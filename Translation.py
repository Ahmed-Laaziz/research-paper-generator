from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

class Translator:
    def __init__(self, model_name, src_lang, tgt_lang):
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.translator = pipeline('translation', model=self.model, tokenizer=self.tokenizer,
                                   src_lang=src_lang, tgt_lang=tgt_lang, max_length=450)

    def translate_text(self, text):
        return self.translator(text)
