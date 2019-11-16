import os
import library.scraper as scraper
import library.genius as genius
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from library.config import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def main():
    return render_template('index.html',
                           my_string="Wheeeee!",
                           my_list=[0,1,2,3,4,5])

@socketio.on('my event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    # app.run(debug=True)

    genius.get_songs()

    # for song, url in LIBRARY.items():
    #     page = scraper.get_lyrics_properties(song, url)
    #     list = scraper.generate_lyrics_tree(page)
