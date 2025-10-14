from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__, template_folder='temp')
app.secret_key='1234'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html', title='Home', pageName='home.html')

@app.route('/chat/<room>')
def chat(room):
    uid = request.args['uid']
    session['uid'] = uid
    session['room'] = room
    room_names  = ['친구', '가족', '회사']
    room_name = room_names[int(room)]
    return render_template('index.html', title='채팅방', pageName='chat.html', 
                           room=room_name, uid=uid)

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

@socketio.on('left', namespace='/chat')
def left():
    uid = session['uid']
    room = session['room']
    msg = f'{uid}님 퇴장하셨습니다.'
    emit('status', {'msg':msg}, room=room)
    leave_room(room)
    
if __name__=='__main__':
    socketio.run(app, port=5000, debug=True)