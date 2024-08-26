from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, join_room, emit

app = Flask(__name__)
app.secret_key='mysecret'
socketio = SocketIO(app)

@app.route('/')
def index():
  return 'Hello'

@socketio.on('joined', namespace='/chat')
def joined(message):
  uid=session['uid']
  room=session['room']
  print(uid, room)
  join_room(room)
  emit('status', {'msg': uid + '님 입장하셨습니다.'}, room=room)

@socketio.on('left', namespace='/chat')
def left(message):
  room = session['room']
  uid = session['uid']
  emit('status', {'msg':uid + '님 퇴장하셨습니다.'}, room=room)

@socketio.on('text', namespace='/chat')
def text(message):
  room = session['room']
  uid = session['uid']
  msg = message.get('msg')
  emit('message', {'msg':uid + ":" + msg}, room=room)
  
@app.route('/chat/<room>') #/chat/친구?uid=blue
def chat(room):
  uid=request.args['uid']
  session['room'] = room
  session['uid'] = uid

  return render_template('chat.html', title='채팅룸', room=room)


if __name__ == '__main__':
  socketio.run(app, debug=True, port=5000)
