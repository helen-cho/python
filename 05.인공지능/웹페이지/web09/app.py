from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__, template_folder='temp', static_folder='static')


@app.route('/')
def index():
    return render_template('index.html', pageName='home.html', title='감성분석')

if __name__=='__main__':
    app.run(port=5000, debug=True)