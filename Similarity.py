import spacy

# Load the language model
nlp = spacy.load('en_core_web_md')

# Define two sentences
sentence1 = "The quick brown fox jumps over the lazy dog."
sentence2 = "A fast brown fox leaps over a sleepy canine."

# Process the sentences with spaCy
doc1 = nlp(sentence1)
doc2 = nlp(sentence2)

# Compute the similarity between the sentences using the vector similarity (cosine similarity)
similarity = doc1.similarity(doc2)

print(f"Similarity: {similarity:.2f}")
