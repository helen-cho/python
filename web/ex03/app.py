from flask import Flask, render_template
from routes import scrap, crawl

app = Flask(__name__, template_folder="templates")
app.register_blueprint(scrap.bp)
app.register_blueprint(crawl.bp)

@app.route("/")
def index():
  return render_template('index.html', title='홈페이지', pageName='home.html')


if __name__ == '__main__':
  app.run(port=5000, debug=True)