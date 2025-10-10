from flask import Flask, render_template
from routes import linear, multi, poly

app = Flask(__name__, template_folder='temp', static_folder='static')

app.register_blueprint(linear.bp)
app.register_blueprint(multi.bp)
app.register_blueprint(poly.bp)

@app.route('/')
def index():
    return render_template('index.html', pageName='home.html', title='자기소개')

if __name__=='__main__':
    app.run(port=5000, debug=True)