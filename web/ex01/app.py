from flask import Flask

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
  return "hello.........."


if __name__ == '__main__':
  app.run(port=5000, debug=True)