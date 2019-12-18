import lyricsgenius
from collections import OrderedDict
from library.config import *

def dedupe_blocks(lyrics_list):
    new_lyrics_list = []
    for block in lyrics_list:
        lyrics_set = {}
        new_block = []
        for line in block:
            if line not in lyrics_set:
                lyrics_set[line] = True
                new_block.append(line)
        new_lyrics_list.append(new_block)
    return new_lyrics_list

def get_songs(song, artist):
    genius = lyricsgenius.Genius(CLIENT_ACCESS_TOKEN)
    lyrics = genius.search_song(song, artist).lyrics.split('\n\n')

    lyrics_list = []
    for block in lyrics:
        if any(ele in block for ele in BLOCK_TYPES):
            lyrics_list.append(block.splitlines()[1:])
        else:
            lyrics_list[-1].append(block)

    lyrics_list = dedupe_blocks(lyrics_list)
    return lyrics_list
