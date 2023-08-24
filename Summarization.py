from transformers import pipeline

class TextSummarizer:
    def __init__(self):
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    def summarize_text(self, text):
        return self.summarizer(text, max_length=130, min_length=10, do_sample=False)
