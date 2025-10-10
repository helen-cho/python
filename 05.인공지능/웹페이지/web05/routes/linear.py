from flask import Blueprint, render_template, request
from sklearn.linear_model import LinearRegression, SGDRegressor
import pandas as pd

bp=Blueprint('linear', __name__, url_prefix='/linear')
path = bp.root_path

def model_reg():
    dataset = pd.read_csv('data/LinearRegressionData.csv')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    reg = LinearRegression()
    reg.fit(X, y)
    return reg

def model_sgd():
    dataset = pd.read_csv('data/LinearRegressionData.csv')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    sgd = SGDRegressor()
    sgd.fit(X, y)
    return sgd

#sgd = model_sgd()
@bp.route('/sgd/predict')
def sgd_predict():
    sgd = model_sgd()
    hour = float(request.args['hour'])
    pred=sgd.predict([[hour]])
    return f'{pred[0]:.2f}'

#reg = model_reg()
@bp.route('/reg/predict')
def reg_predict():
    reg = model_reg()
    hour = float(request.args['hour'])
    pred=reg.predict([[hour]])
    return f'{pred[0]:.2f}'

#최소제곱법 페이지출력
@bp.route('/reg')
def reg():
    return render_template('index.html', pageName='reg.html', 
                           title='최소제곱법(선형회귀)')

#경사하강법 페이지출력
@bp.route('/sgd')
def sgd():
    return render_template('index.html', pageName='sgd.html',
                           title='경사하강법(선형회귀)')