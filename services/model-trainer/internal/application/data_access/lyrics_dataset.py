import pandas as pd

class LyricsDataset:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_lyrics_by_artist(self, artist_name):
        data = pd.read_csv(self.file_path)
        artist_data = data[data['ALink'] == '/' + artist_name + '/']
        lyrics = artist_data['Lyric'].tolist()
        return "\n".join(lyrics)