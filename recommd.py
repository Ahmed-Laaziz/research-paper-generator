import os
import json
import numpy as np 
import pandas as pd
from itertools import islice 
from scipy.spatial.distance import euclidean
from sklearn.feature_extraction.text import TfidfVectorizer # for featurizing text
from sklearn.metrics.pairwise import cosine_similarity # for getting similarity score
import tensorflow as tf
import tensorflow_hub as hub
import faiss
from rank_bm25 import BM25Okapi
model_url = "https://www.kaggle.com/models/google/universal-sentence-encoder/frameworks/TensorFlow2/variations/universal-sentence-encoder/versions/1"
embed = hub.load(model_url)
sentence_encoder_layer = hub.KerasLayer(model_url, input_shape=[], dtype=tf.string, trainable=False, name="use")

# Load your data
def extract_data(datapath):
    with open(datapath, 'r') as datafile:
        for line in datafile:
            yield line
BASE_PATH = 'C:/Users/ULTRAPC/Documents/Research-paper-recommender-system'
FILE_NAME =  'metadata.json'
FILE_PATH = os.path.join(BASE_PATH, FILE_NAME)
data_gen = extract_data(FILE_PATH)

def fetch_n_records(data_gen, chunksize=500):
    return [json.loads(record) for record in islice(data_gen, chunksize)]

CHUNK_SIZE = 250000
data_records = fetch_n_records(data_gen, CHUNK_SIZE)

# Preprocess your data and create necessary variables
# Define useful features
useful_features = ['id', 'title', 'categories', 'abstract', 'authors', 'update_date']

# Create DataFrames
df = pd.DataFrame(data_records)
final_df = df[useful_features]

# Convert the 'update_date' column to a datetime format
final_df['update_date'] = pd.to_datetime(final_df['update_date'])

# Combine title and abstract for text processing
final_df['text_combined'] = final_df['title'] + ' ' + final_df['abstract']

# Initialize the TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer(max_features=10000)

# Fit the vectorizer on the combined text
tfidf_matrix = tfidf_vectorizer.fit_transform(final_df['text_combined'])

# Initialize BM25Okapi
bm25 = BM25Okapi([doc.split() for doc in final_df['text_combined']])

# Load your precomputed embeddings
abstracts = df["abstract"].to_list()
embeddings = []
batch_size = 3000
num_batches = len(abstracts) // batch_size
#compute Embeddings in batches
for i in range(num_batches):
    batch_abstracts = abstracts[i * batch_size: (i + 1) * batch_size]
    batch_embeddings = sentence_encoder_layer(batch_abstracts)['outputs']  
    embeddings.extend(batch_embeddings.numpy())

#embeddings for remaining abstracts
remaining_abstracts = abstracts[num_batches * batch_size:]
if len(remaining_abstracts) > 0:
    remaining_embeddings = sentence_encoder_layer(remaining_abstracts)['outputs'] 
    embeddings.extend(remaining_embeddings.numpy())

#convert embeddings to a single NumPy array
embeddings = np.array(embeddings)
y = df.index


# Convert embeddings to float32 arrays
embeddings = np.array(embeddings, dtype=np.float32)

# Initialize the FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

def get_recommendations_use_faiss(query_title, index, df, num_rec):
    query_embedding = embed([query_title])['outputs'][0].numpy()  # Extract the 1-D array

    _, nearest_indices = index.search(np.array([query_embedding]), num_rec + 1)  # Pass the 1-D query embedding

    recommendations = []
    for i in range(1, num_rec + 1):
        recommended_idx = nearest_indices[0][i]
        recommended_title = df['title'][recommended_idx]
        recommended_authors = df['authors'][recommended_idx]
        recommended_cat = df['categories'][recommended_idx]
        recommended_abstract = df['abstract'][recommended_idx]
        recommended_id = df['id'][recommended_idx]
        recommended_url = f"https://arxiv.org/pdf/{recommended_id}.pdf"

        recommended_embedding = embeddings[recommended_idx]  # Use the precomputed embeddings
        similarity_score = -euclidean(query_embedding, recommended_embedding)

        recommendation = {
            'title': recommended_title,
            'authors': recommended_authors,
            'abstract': recommended_abstract,
            'id': recommended_id,
            'link': recommended_url,
            'Category': recommended_cat,
            'similarity_score': similarity_score
        }
        recommendations.append(recommendation)

    recommendations.sort(key=lambda x: x['similarity_score'], reverse=True)
    return recommendations



def get_recommendations_tfidf_bm25(input_text: str, tfidf_matrix, bm25, final_df, num_rec: int):
    # Transform the input text using the fitted TF-IDF vectorizer
    tfidf_matrix_input = tfidf_vectorizer.transform([input_text])
    
    # Calculate BM25 similarity scores
    bm25_sim = bm25.get_scores(input_text.split())
   
    # Calculate TF-IDF similarity scores
    tfidf_sim = cosine_similarity(tfidf_matrix_input, tfidf_matrix)
    
    # Mix TF-IDF and BM25 scores (you can adjust the weights as needed)
    mix_score = 0.7 * tfidf_sim + 0.3 * bm25_sim
    
    # Get indices of the top recommendations based on mixed scores
    top_n_idx = np.argsort(-mix_score[0])[:num_rec]  # Sort the mix_score array
    
    # Get corresponding paper IDs and mix scores of the top recommendations
    top_n_info = [
        {
            'id': final_df['id'][idx],
            'mix_score': mix_score[0, idx],  # Add the mix score to the info
            'title': final_df['title'][idx],
            'authors': final_df['authors'][idx],
            'Category' : final_df['categories'][idx],
            'abstract': final_df['abstract'][idx],
            'link': f"https://arxiv.org/pdf/{final_df['id'][idx]}.pdf"
            
        }
        for idx in top_n_idx
    ]
     
    return top_n_info

def get_recommandations(query_title, index, tfidf_matrix, bm25, final_df, num_rec):
    recommendations_tfidf_bm25 = get_recommendations_tfidf_bm25(query_title, tfidf_matrix, bm25, final_df, num_rec)
    recommendations_faiss = get_recommendations_use_faiss(query_title, index, final_df, num_rec)

    # Create alternating mixed recommendations starting with the first approach
    mixed_recommendations = []

    for i in range(num_rec):
        if i % 2 == 0:
            mixed_recommendations.append(recommendations_tfidf_bm25.pop(0))
        else:
            mixed_recommendations.append(recommendations_faiss.pop(0))

    return mixed_recommendations