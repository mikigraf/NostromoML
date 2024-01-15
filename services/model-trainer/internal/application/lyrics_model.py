import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from transformers import TFGPT2LMHeadModel, pipeline, GPT2Tokenizer

class LyricsModel:
    def __init__(self):
        self.model = TFGPT2LMHeadModel.from_pretrained("gpt2")
        self.optimizer = tf.keras.optimizers.Adam(learning_rate=5e-5)
        self.loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    def train(self, tokens):
        max_length = 128 
        tokens_padded = pad_sequences(tokens, maxlen=max_length, padding='post', truncating='post')

        tf_dataset = tf.data.Dataset.from_tensor_slices((tokens_padded, tokens_padded))
        tf_dataset = tf_dataset.shuffle(len(tokens_padded)).batch(4)

        self.model.compile(optimizer=self.optimizer, loss=self.loss)
        self.model.fit(tf_dataset, epochs=7)

        self.model.save_pretrained("./gpt2-finetuned")

    def generate(self, prompt):
        device = 'cuda' if tf.config.list_physical_devices('GPU') else 'cpu'
        with tf.device(device):
            model = TFGPT2LMHeadModel.from_pretrained("./gpt2-finetuned")
            generator = pipeline('text-generation', model=model, tokenizer=self.tokenizer, device=0 if device == 'cuda' else -1)

            generated_text = generator(prompt, max_length=255)
            return generated_text[0]['generated_text']
