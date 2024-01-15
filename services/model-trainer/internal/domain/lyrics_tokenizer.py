from transformers import GPT2Tokenizer

class LyricsTokenizer:
    def __init__(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    def tokenize(self, text):
        tokens = self.tokenizer.encode(
            text, return_tensors='tf', 
            max_length=self.tokenizer.model_max_length, truncation=True
        )
        return tokens