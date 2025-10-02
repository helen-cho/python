from flask import Flask, render_template, request
import pandas as pd
import FinanceDataReader as fdr

app = Flask(__name__, template_folder='temp', static_folder='static')

@app.route('/img1')
def img1():
    code = request.args['code']
    start = request.args['start']
    end = request.args['end']
    df = fdr.DataReader(code, start, end)


@app.route('/img2')
def img2():
    code = request.args['code']
    start = request.args['start']
    end = request.args['end']
    df = fdr.DataReader(code, start, end)


def getData(code, start, end):
    code = request.args['code']
    start = request.args['start']
    end = request.args['end']
    df = fdr.DataReader(code, start, end)
    return df

@app.route('/data')
def data():
    code = request.args['code']
    start = request.args['start']
    end = request.args['end']
    df = getData(code, start, end)
    df = df.head()
    table = df.to_html(classes='table table-striped table-hover')
    return table

@app.route('/')
def index():
    return render_template('index.html', pageName='home.html', title='주가예측')

if __name__=='__main__':
    app.run(port=5000, debug=True)