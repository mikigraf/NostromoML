from internal.application.data_access import LyricsDataset
from internal.domain.lyrics_tokenizer import LyricsTokenizer
from internal.application.lyrics_model import LyricsModel

def train_and_generate_lyrics(artist_name, prompt):
    lyrics_dataset = LyricsDataset('lyrics-data.csv')
    lyrics = lyrics_dataset.get_lyrics_by_artist(artist_name)

    tokenizer = LyricsTokenizer()
    tokens = tokenizer.tokenize(lyrics)

    lyrics_model = LyricsModel()
    # lyrics_model.train(tokens)
    generated_text = lyrics_model.generate(prompt)
    print(generated_text)

if __name__ == "__main__":
    train_and_generate_lyrics('drake', 'Write a simple rap song in the style of Drake')