import openai

# Set your OpenAI API key
openai.api_key = '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'

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import openai

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Read OpenAI API key from a text file
with open("openai_api_key.txt", "r") as file:
    openai_api_key = file.read().strip()

# Set your OpenAI API key
openai.api_key = openai_api_key

#TITLE
def generate_title(field):
    # Generate text using the GPT-3.5 model
    prompt = f"i want to write a research paper about {field} can you give me in one sentence a title ?"
    response = openai.Completion.create(
        engine="text-davinci-003",  # Specify the GPT-3.5 model
        prompt=prompt,
        max_tokens=100  # Adjust the desired length of generated text
    )
    title =(response.choices[0].text).replace('\n', '').replace('\"', '')
    return title

#ABSTRACT
def generate_abstract(title):
    prompt = "can you give me an abstract for my research paper titled : " + title + "?"
    response = openai.Completion.create(
        engine="text-davinci-003",  # Specify the GPT-3.5 model
        prompt=prompt,
        max_tokens=100  # Adjust the desired length of generated text
    )
    abstract = (response.choices[0].text).replace('\n', '').replace('\"', '')
    return abstract

#INTRODUCTION
def generate_introduction(title):
    prompt = "can you give me an introduction for my research paper titled : " + title + "?"
    response = openai.Completion.create(
        engine="text-davinci-003",  # Specify the GPT-3.5 model
        prompt=prompt,
        max_tokens=100  # Adjust the desired length of generated text
    )
    introduction = (response.choices[0].text).replace('\n', '').replace('\"', '')
    return introduction

#BODY
def generate_body(title):
    prompt = "can you suggest me the body of my research paper titled : " + title + "?"
    response = openai.Completion.create(
        engine="text-davinci-003",  # Specify the GPT-3.5 model
        prompt=prompt,
        max_tokens=200  # Adjust the desired length of generated text
    )
    body = (response.choices[0].text).replace('\n', '').replace('\"', '')
    return body

#CONCLUSION
def generate_conclusion(title):
    prompt = "can you give me a conclusion for my research paper titled : " + title + "?"
    response = openai.Completion.create(
        engine="text-davinci-003",  # Specify the GPT-3.5 model
        prompt=prompt,
        max_tokens=100  # Adjust the desired length of generated text
    )
    conclusion = (response.choices[0].text).replace('\n', '').replace('\"', '')
    return conclusion

#REFERENCES
def generate_references(title):
    prompt = "can you give me some interesting references for my research paper titled : " + title + "?"
    response = openai.Completion.create(
        engine="text-davinci-003",  # Specify the GPT-3.5 model
        prompt=prompt,
        max_tokens=100  # Adjust the desired length of generated text
    )
    references = (response.choices[0].text).replace('\n', '').replace('\"', '')
    return references

@app.get("/")
def generate_research_paper(field : str):
    title = generate_title(field)
    abstract = generate_abstract(title)
    introduction = generate_introduction(title)
    body = generate_body(title)
    conclusion = generate_conclusion(title)
    references = generate_references(title)
    response_data = {
        "title": title,
        "abstract": abstract,
        "introduction":introduction,
        "body":body,
        "conclusion":conclusion,
        "references":references
    }
    return JSONResponse(content=response_data)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)


