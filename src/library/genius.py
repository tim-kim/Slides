import lyricsgenius
from collections import OrderedDict
from library.config import *

def get_songs():
    genius = lyricsgenius.Genius(CLIENT_ACCESS_TOKEN)
    song = 'This I Believe (The Creed)'
    artist = 'Hillsong Worship'

    # lyrics = genius.search_song(song, artist).lyrics
    with open('lyrics.txt', 'r') as f:
        lyrics = f.read()
        lyrics_list = lyrics.splitlines()

        blocks = []
        blocks.append([])
        block_index = 0
        for entity in lyrics_list[1:]:
            if ('[' in entity) and (']' in entity):
                blocks.append([])
                block_index += 1
            else:
                if len(entity) > 0:
                    blocks[block_index].append(entity)

        slides = []
        for block in blocks:
            if len(''.join(block)) > CHAR_LIMIT:
                s = set()
                dupe_index = ''
                for index, entity in enumerate(block):
                    if entity in s:
                        # Add the first half of big block to slides
                        dupe_index = index
                        slides.append('\n'.join(block[:dupe_index]))
                        break
                    else:
                        s.add(entity)
                # Add the second half of big block to slides
                slides.append('\n'.join(block[dupe_index:]))
            else:
                slides.append('\n'.join(block))

    with open('out.txt', 'w') as f:
        for thing in slides:
            f.write(thing + '\n\n')

    # Write to a lyrics.txt file
    # with open('lyrics.txt', 'w') as f:
    #     for song, artist in LIBRARY.items():
    #         lyrics = genius.search_song(song, artist).lyrics
    #         f.write(lyrics + '\n\n')
