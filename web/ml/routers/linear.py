from flask import Blueprint, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression

bp = Blueprint('linear', __name__, url_prefix='/linear')

@bp.route('/page1')
def page1():
  return render_template(
    'index.html', title='선형회귀(Linear)', pageName='linear/page1.html')

@bp.route('/page3')
def page3():
  return render_template(
    'index.html', title='다중선형회귀(Multiple)', pageName='linear/page3.html')

@bp.route('/result1')
def result1():
  hours = float(request.args['hours'])
  dataset = pd.read_csv('static/data/LinearRegressionData.csv')
  X = dataset.iloc[:, :-1].values
  y = dataset.iloc[:, -1].values
  reg = LinearRegression()
  reg.fit(X, y)
  result = reg.predict([[hours]])
  return str(round(result[0], 2))