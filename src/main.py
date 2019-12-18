import sys, os
import library.scraper as scraper
import library.genius as genius
import library.powerpoint as pp
import library.transcribe as transcribe
from collections import OrderedDict
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from library.config import *
from pptx import Presentation

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def main():
    return render_template('index.html')

@socketio.on('connected event', namespace='/main')
def handle_connected_event(json, methods=['GET', 'POST']):
    print('received connected event: ' + str(json))

@socketio.on('message event', namespace='/main')
def handle_message_event(json, methods=['GET', 'POST']):
    print('message is: ' + str(json['message']))
    emit('server response', json, broadcast=True)

if __name__ == '__main__':
    LIBRARY = OrderedDict()
    with open('setlist.txt', 'r') as f:
        setlist = f.readlines()
        for entity in setlist:
            e = entity.split(' / ')
            song = e[0]
            artist = e[1]
            LIBRARY[song] = artist

    prs = Presentation()

    for song, artist in LIBRARY.items():
        pp.create_title_slide(prs, song.upper(), artist.upper())
        lyrics = genius.get_songs(song, artist)
        for block in lyrics:
            pp.create_lyric_slide(prs, block)

    prs.save('test.pptx')






    # socketio.run(app, debug=True)
    ####
    # for song, url in LIBRARY.items():
    #     page = scraper.get_lyrics_properties(song, url)
    #     list = scraper.generate_lyrics_tree(page)
