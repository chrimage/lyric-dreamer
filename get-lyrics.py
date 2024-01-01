
from lyricsgenius import Genius

genius = Genius(api_key)

genius.remove_section_headers = True # remove section headers (e.g. [Chorus]) from lyrics when searching

# input artist name
artist_name = input("Enter artist name: ")

# input song name
song_name = input("Enter song name: ")

# search for song
song = genius.search_song(song_name, artist_name)

# jsonify lyrics
lyrics = song.lyrics
lines = lyrics.split("\n")

# remove first line
lines = lines[1:]

# remove empty lines
lines = list(filter(lambda x: x != "", lines))

# remove the string "22Embed" from the last line
lines[-1] = lines[-1][:-7]

# print lines
for line in lines:
    print(line)