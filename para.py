import pickle
import nltk
from nltk.tokenize import sent_tokenize
from fastapi import FastAPI
import uvicorn
import os
from parrot import Parrot 
from uvicorn import Config, Server
from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
#Init models
with open("parrot_model.pkl", 'rb') as f:
    parrot= pickle.load(f)
def create_paraphrase(full_text):
    phrases = [x.strip() for x in full_text.split('.')]
    print(phrases)
    output_phrases = []
    for phrase in phrases:
        if (len(phrase) >1 ):
            print("-"*100)
            print("Input_phrase: ", phrase)
            print("-"*100)
            para_phrases = parrot.augment(input_phrase=phrase)
            try:
                for para_phrase in para_phrases:
                    (x, y) = para_phrase
                    print(x, y)
                    x = x[0].upper() + x[1:] # captialise
                    output_phrases.append(x)
                    break # just get the first phrase
            except:
                print("Exception occured with this one.")
                output_phrases.append(phrase)
    
    return ".".join(output_phrases)
def paraphrase_paragraph(input_paragraph):
    phrases = sent_tokenize(input_paragraph)

    result = []

    for phrase in phrases:
        para_phrases = parrot.augment(input_phrase=phrase)
        if para_phrases:
            best_para_phrase, best_score = max(para_phrases, key=lambda x: x[1])
            result.append(best_para_phrase)
        else:
            result.append(phrase)
        rejoined_paragraph = ""
    for i  in range(len(result)):
      rejoined_paragraph+=result[i]+" "
    return(rejoined_paragraph)
app = FastAPI()
app = FastAPI()
app.mount("/assets", StaticFiles(directory="front-end/assets"), name="assets")
app.mount("/vendor", StaticFiles(directory="front-end/vendor"), name="vendor")

@app.get("/")
def read_index(request: Request):
     return FileResponse("front-end/index.html")

@app.get("/authentification")
def read_generation():
    return FileResponse("front-end/authentification.html")

@app.get("/generation")
def read_generation():
    return FileResponse("front-end/generation.html")

@app.get("/paraphrase")
def read_paraphrase():
    return FileResponse("front-end/paraphrase.html")
@app.post("/paraphraser")
def paraphrase(input_data: dict):
    input_paragraph = input_data.get("input_paragraph")
    paraphrased_paragraph = create_paraphrase(input_paragraph)
    print(paraphrased_paragraph)
    return {"paraphrased_paragraph": paraphrased_paragraph}
@app.get("/recommendation")
def read_recommendation():
    return FileResponse("front-end/recommendation.html")
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)











  
