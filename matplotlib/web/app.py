from flask import Flask, render_template, send_file
from graph import graph1, graph2, graph3
from io import BytesIO

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.use('Agg') #Agg 백엔드는 GUI가 필요없는 이미지 생성에 적합

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
  return render_template('index.html', title='데이터 시각화')

@app.route('/page1')
def page1():
  df= graph1()
  return df.to_html(classes='table table-hover table-striped table-bordered', table_id='tbl1') 

@app.route('/image1')
def image1():
  df = graph1()
  plt.bar(df['영화'], df['평점'])
  plt.xticks(rotation=90)
  plt.xlabel('영화제목')
  plt.ylabel('평점')
  plt.title('국내 Top8 영화 평점 정보')

  img = BytesIO()
  plt.savefig(img, format='png', dpi=200)
  plt.close()
  img.seek(0)
  return send_file(img, mimetype='image/png')
  
@app.route('/page2')
def page2():
  df = graph2()
  return df.to_html(classes='table table-hover table-striped table-bordered', table_id='tbl1') 

@app.route('/image2')
def image2():
  df_group = graph2()
  plt.plot(df_group.index, df_group['평점'], marker='o')
  plt.xticks([2005, 2010, 2015, 2020])
  plt.ylim(7, 10)

  img = BytesIO()
  plt.savefig(img, format='png', dpi=200)
  plt.close()
  img.seek(0)
  return send_file(img, mimetype='image/png')

@app.route('/page3')
def page3():
  df = graph3()
  return df.to_html(classes='table table-hover table-striped table-bordered', table_id='tbl1') 

@app.route('/image3')
def image3():
  df = graph3()
  fig, ax1 = plt.subplots(figsize=(10, 5))
  ax1.bar(df.index, df['출생아 수'], color='orange')
  ax1.set_ylabel('출생아 수(천명)')
  ax1.set_ylim(250, 550)
  ax1.set_yticks([300, 400, 500, 600])
  for idx, val in enumerate(df['출생아 수']):
    ax1.text(idx, val+5, val, ha='center')

  ax2 = ax1.twinx()
  ax2.set_ylabel('합계 출산율')
  ax2.plot(df.index, df['합계 출산율'], color='green', marker='o', ms=15, lw=5, mec='w', mew=5)
  ax2.set_ylim(0, 1.5)
  ax2.set_yticks([0, 1, 1.5])
  for idx, val in enumerate(df['합계 출산율']):
    ax2.text(idx, val+0.05, val, ha='center')

  img = BytesIO()
  plt.savefig(img, format='png', dpi=200)
  plt.close()
  img.seek(0)
  return send_file(img, mimetype='image/png')

if __name__=='__main__':
  app.run(port=5000, debug=True)