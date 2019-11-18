import os
import library.scraper as scraper
import library.genius as genius
import library.transcribe as transcribe
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from library.config import *

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
    socketio.run(app, debug=True)

    # genius.get_songs()

    # for song, url in LIBRARY.items():
    #     page = scraper.get_lyrics_properties(song, url)
    #     list = scraper.generate_lyrics_tree(page)
