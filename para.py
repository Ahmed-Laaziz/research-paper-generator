import pickle
import nltk
from nltk.tokenize import sent_tokenize
from fastapi import FastAPI
import uvicorn
import os
from parrot import Parrot 
from uvicorn import Config, Server
#Init models
with open("parrot_model.pkl", 'rb') as f:
    parrot= pickle.load(f)
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
@app.get("/")
def test():
  return "working"
@app.post("/paraphrase")
def paraphrase(input_data: dict):
    input_paragraph = input_data.get("input_paragraph")
    paraphrased_paragraph = paraphrase_paragraph(input_paragraph)
    return {"paraphrased_paragraph": paraphrased_paragraph}



if __name__ == "__main__":
    config = Config(app=app, host="0.0.0.0", port=os.environ.get("PORT", 8000))
    server = Server(config)
    server.run()


  
