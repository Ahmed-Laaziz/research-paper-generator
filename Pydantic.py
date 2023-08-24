from pydantic import BaseModel

class AbstractRequest(BaseModel):
    abstract_text: str
    title: str
    words_to_generate : int

class TitleRequest(BaseModel):
    field: str

class ChatBotAnswerRequest(BaseModel):
    question: str

class TranslatorAnswerRequest(BaseModel):
    text: str
    src: str
    tgt: str

class SummarizerAnswerRequest(BaseModel):
    text: str
