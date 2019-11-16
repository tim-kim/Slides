import requests
from library.config import *
from html2text import *

def get_lyrics_properties(song, url):
    title = '**"{}"**'.format(song)
    r = requests.get(url)
    return {'html': r.text, 'title': title }

# def check_for_strip_line(line):
#     if line in ['x2' ... ]

def generate_lyrics_tree(page):
    text = HTML2Text()
    text.ignore_links = True

    t = text.handle(page['html'])
    t = t.split(BOTTOM_SPLIT)[0]
    t = t.split(page['title'])[1]

    list_v1 = t.splitlines()
    list_v1 = list(map(str.strip, list_v1)) # strips whitespace in all items

    list_v2 = []
    block = ""
    is_block = False
    for line in list_v1:
        if len(line) > 0:
            if len(block) == 0:
                block = line
            else:
                block = '\n'.join([block, line])
            is_block = True
        elif len(line) == 0 and is_block:
            list_v2.append(block)
            block = ""
            is_block = False
    return list_v2
