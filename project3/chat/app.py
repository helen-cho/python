from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__, template_folder='temp')
app.secret_key='1234'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html', title='채팅방', pageName='home.html')

if __name__=='__main__':
    socketio.run(app, port=5000, debug=True)