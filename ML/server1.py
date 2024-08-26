from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, join_room, emit
import time
from scrap import weather_temp, exechage_rate, stock

app = Flask(__name__)
app.secret_key='mysecret'
socketio = SocketIO(app)

@app.route('/')
def index():
  return 'Hello'

@socketio.on('joined', namespace='/chat')
def joined(message):
  room=session['room']
  join_room(room)
  emit('status', {'msg': room + '님 입장하셨습니다.'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
  room = session['room']
  uid = session['uid']
  msg = message.get('msg')
  emit('message', {'msg':uid + ":" + msg}, room=room)
  answer_text = answer(msg)
  emit('message', {'msg':"[인공지능]:" + answer_text}, room=room)


def answer(input_text):
  answer_text = ''
  if '안녕' in input_text:
    answer_text='안녕하세요! 반갑습니다.'
  elif '날씨' in input_text:
    answer_text=weather_temp()
  elif '환율' in input_text:
    rate = exechage_rate()  
    answer_text = '1달러 환율은 ' + rate + "입니다."
  elif '주식' in input_text:
    answer_text = stock(input_text)
  else:
    answer_text='다시한번 말씀해 주시겠어요?'  
  time.sleep(1)
  return answer_text

@app.route('/chat') #/chat?uid=blue
def chat():
  uid=request.args['uid']
  session['room'] = uid
  return render_template('chat.html', title='채팅룸', room='인공지능')

if __name__ == '__main__':
  socketio.run(app, debug=True, port=5000)