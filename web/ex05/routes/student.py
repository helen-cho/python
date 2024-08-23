from flask import Blueprint, render_template, request, send_file
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' #맑은 고딕
matplotlib.rcParams['font.size'] = 15 #글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False #한글 폰트 사용 시 마이너스 글자가 깨지는 현상을 해결


bp = Blueprint('student', __name__, url_prefix='/student')


def read_data():
  df = pd.read_csv('data/score.csv')
  df['학년'] = [3,3,3,1,1,3,2,2]
  df.set_index('지원번호', drop=True, inplace=True)
  df.fillna('', inplace=True)
  return df

@bp.route('/search/data')
def search_data():
  df = read_data()
  
  args = request.args
  key = args['key']
  word = args['word']
  
  if word == '':
    df1 = df
  else:  
    filt = df[key].str.contains(word, case=False)
    df1 = df[filt]

  #table = df.to_html(classes='table', table_id='tbl1')
  json = df1.to_json(orient='records')
  return json

@bp.route('/search')
def search():
  return render_template(
    'index.html',
    title='학생검색',
    pageName='student/search.html')

@bp.route('/info')
def info():
  df = read_data()
  df1 = df.loc[:, ['학교','이름', '국어', '영어', '수학']]
  df1['평균'] = round((df['국어'] + df['영어'] + df['수학'])/3,2)
  df3 = df.groupby(['학교','학년'])[['국어','영어','수학']].mean()

  df2 = df.loc[:, ['학교', '이름', '키', 'SW특기']]
  table1 = df1.to_html(classes='table', table_id='tbl1')
  table2 = df2.to_html(classes='table', table_id='tbl2')
  table3 = df3.to_html(classes='table', table_id='tbl3')

  return render_template(
    'index.html', title='학생정보', pageName='student/info.html',
    table1=table1, table2=table2, table3=table3)

@bp.route('/graph')
def graph():
  return render_template(
    'index.html', 
    title='학생성적그래프',
    pageName='/student/graph.html'
  )

@bp.route('/graph/image')
def graph_image():
  import numpy as np
  from io import BytesIO

  df = read_data()
  index = np.arange(df.shape[0])
  w = 0.25
  plt.figure(figsize=(10, 5))
  plt.bar(index-w, df['국어'], width=w, label='국어')
  plt.bar(index, df['영어'], width=w, label='영어')
  plt.bar(index+w, df['수학'], width=w, label='수학')
  plt.xticks(index, df['이름'], rotation=0)
  plt.legend(ncols=3)
  
  img = BytesIO()
  plt.savefig(img, format='png', dpi=200)
  img.seek(0)
  return send_file(img, mimetype='image/png')