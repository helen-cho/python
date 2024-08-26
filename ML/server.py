from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello'

@app.route('/chat')
def chat():
  return render_template('chat.html', title='채팅룸')


if __name__ == '__main__':
  app.run(debug=True, port=5000)
