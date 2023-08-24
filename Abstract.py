from transformers import AutoTokenizer, AutoModelForCausalLM, GPT2Config
from transformers import pipeline

class AbstractGenerator:
    def __init__(self):
        #model_path = "C:/Users/ADMIN/PycharmProjects/pythonProject/models/output_dir_gpt2_fineTuned_model_abstracts"
        self.tokenizer = AutoTokenizer.from_pretrained("C:/Users/ADMIN/PycharmProjects/pythonProject/models/output_dir_gpt2_fineTuned_model_abstracts")
        model_config = GPT2Config.from_pretrained("C:/Users/ADMIN/PycharmProjects/pythonProject/models/output_dir_gpt2_fineTuned_model_abstracts/config.json")
        self.model = AutoModelForCausalLM.from_pretrained("C:/Users/ADMIN/PycharmProjects/pythonProject/models/output_dir_gpt2_fineTuned_model_abstracts/pytorch_model.bin", config=model_config)

        # Create a text generation pipeline
        self.text_generator = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer)

    def generate_abstract(self, title, max_length=20, prompt=None):
        if prompt is None:
            prompt = f"Q: Can you give me an abstract for my research paper with the Title:{title}?"
        #else:
        #    prompt = f"{prompt} {title}?"

        # Tokenize the sentence
        tokens = self.tokenizer(prompt, return_tensors="pt")["input_ids"]

        # Get the number of tokens
        num_tokens = tokens.shape[1] if len(tokens.shape) > 1 else tokens.shape[0]

        # Generate text using the fine-tuned model
        generated_text = self.text_generator(prompt, max_length=max_length + num_tokens, num_return_sequences=1)

        return generated_text[0]['generated_text']