from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, emit, join_room, leave_room
from scrapping import answer
from gtts import gTTS
from playsound import playsound
import os

def speak(text):
    file_name='voice.mp3'
    tts_ko = gTTS(text=text, lang='ko')
    tts_ko.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):
        os.remove(file_name)
    
app = Flask(__name__, template_folder='temp')
app.secret_key='1234'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html', title='Home', pageName='home.html')

@app.route('/chat/<uid>')
def chat(uid):
    session['uid'] = uid
    session['room'] = uid
    return render_template('index.html', title='채팅방', pageName='chat.html', 
                           room='인공지능', uid=uid)

@socketio.on('joined', namespace='/chat')
def joined():
    uid = session['uid']
    room = session['room']
    join_room(room)
    msg = f'{uid}님 입장하셨습니다.'
    emit('status', {'msg':msg}, room=room)

@socketio.on('text', namespace='/chat')
def text(data):
    uid = session['uid']
    room = session['room']
    msg = data.get('msg')
    emit('message', {'msg':f'{uid}: {msg}'}, room=room)

    answer_text = answer(msg)
    emit('message', {'msg':f'[인공지능]: {answer_text}'}, room=room)
    speak(answer_text)

@socketio.on('left', namespace='/chat')
def left():
    uid = session['uid']
    room = session['room']
    msg = f'{uid}님 퇴장하셨습니다.'
    emit('status', {'msg':msg}, room=room)
    leave_room(room)
    
if __name__=='__main__':
    socketio.run(app, port=5000, debug=True)