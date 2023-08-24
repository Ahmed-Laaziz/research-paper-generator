import openai
import uvicorn
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import openai

from research_paper.Abstract import AbstractGenerator
from research_paper.Title import TitleGenerator
from research_paper.ChatBot import ChatBotAnswersGenerator
from research_paper.ChatBotNlp import ChatBotAnswersGeneratorNLP
from Translation import Translator
from Summarization import TextSummarizer
from Pydantic import AbstractRequest, TitleRequest, ChatBotAnswerRequest, TranslatorAnswerRequest, SummarizerAnswerRequest

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


#TITLE
def generate_summarize():
    # Generate text using the GPT-3.5 model
    prompt = f"can you summarize for me the research paper please ?"
    response = openai.Completion.create(
        engine="text-davinci-003",  # Specify the GPT-3.5 model
        prompt=prompt,
        max_tokens=150  # Adjust the desired length of generated text
    )
    res =(response.choices[0].text).replace('\n', '').replace('\"', '')
    return res

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
    res = generate_summarize()
    response_data = {
        "title": title,
        "abstract": abstract,
        "introduction":introduction,
        "body":body,
        "conclusion":conclusion,
        "references":references,
        "sum":res
    }
    return JSONResponse(content=response_data)

@app.post("/generate_abstract")
def generate_abstract_from_gpt2(request: AbstractRequest):
    generator = AbstractGenerator()
    #title = "Python as a powerful programming language for Data Science"
    prompt = f"Q: Can you give me an abstract for my research paper with the Title:{request.title}?A: Abstract:" + request.abstract_text
    abstract = generator.generate_abstract(request.title, prompt=prompt, max_length = request.words_to_generate)
    print(prompt)
    # Split the generated text based on "A: Abstract:"
    split_text = abstract.split("A: Abstract:")
    # Extract the text after "A: Abstract:"
    if len(split_text) > 1:
        abstract_text = split_text[1].strip()  # Remove leading/trailing whitespaces
    else:
        abstract_text = "No abstract found."
    print(abstract_text)
    return abstract_text

@app.post("/generate_title")
def generate_abstract_from_gpt2(request: TitleRequest):
    generator = TitleGenerator()
    title = generator.generate_title(field = request.field)
    # Split the generated text based on "A: Abstract:"
    print(title)
    split_text = title.split("A: Title:")
    # Extract the text after "A: Abstract:"
    print(split_text)
    if len(split_text) > 1:
        title_text = (split_text[1].split("Q: Can you"))[0].strip()  # Remove leading/trailing whitespaces
    else:
        title_text = "No title found."
    return title_text

@app.post("/get_chatbot_answer")
def generate_chatbot_answers_from_gpt2(request: ChatBotAnswerRequest):
    generator = ChatBotAnswersGenerator()
    chatAnswer = generator.generate_answer(question = request.question)
    #Split the generated text based on "A: Abstract:"
    split_text = chatAnswer.split("Bot: ")
    # Extract the text after "?"
    print(split_text)
    if len(split_text) > 1:
       #answer = split_text[1].strip()  # Remove leading/trailing whitespaces
       answer = (split_text[1].split("User:"))[0].strip()
    else:
       answer = "No title found."
    return answer

@app.post("/get_chatbot_answer_nlp")
def generate_chatbot_answers_from_gpt2(request: ChatBotAnswerRequest):
    generator = ChatBotAnswersGeneratorNLP()
    chatAnswer = generator.generate_answer(question = request.question)
    #Split the generated text based on "A: Abstract:"
    split_text = chatAnswer.split("Bot: ")
    # Extract the text after "?"
    print(split_text)
    if len(split_text) > 1:
       #answer = split_text[1].strip()  # Remove leading/trailing whitespaces
       answer = (split_text[1].split("User:"))[0].strip()
    else:
       answer = "No title found."
    return answer

@app.post("/get_translation")
def generate_translation(request: TranslatorAnswerRequest):
    translator = Translator("facebook/nllb-200-distilled-600M", src_lang=request.src, tgt_lang=request.tgt)
    return translator.translate_text(text = request.text)[0]['translation_text']

@app.post("/get_summarization")
def generate_summarization(request: SummarizerAnswerRequest):
    summarizer = TextSummarizer()
    return summarizer.summarize_text(request.text[:2048])[0]['summary_text']
"""
@app.get("/get_translation")
def generate_translation(text: str, src:str, tgt:str):
    translator = Translator("facebook/nllb-200-distilled-600M", src_lang=src, tgt_lang=tgt)
    return translator.translate_text(text = text)[0]['translation_text']
"""


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8008)



