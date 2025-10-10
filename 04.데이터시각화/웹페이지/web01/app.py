from flask import Flask, render_template, send_file
from io import BytesIO

import pandas as pd
df = pd.read_csv('c:/python/04.데이터시각화/data/score.csv', index_col='지원번호')

import matplotlib.pyplot as plt
#한글설정
plt.rc('font', family = 'Malgun Gothic')
plt.rc('font', size = 10)
plt.rc('axes', unicode_minus = False)

app = Flask(__name__, template_folder='templates')

@app.route('/graph1') #학생별키 막대그래프
def graph1():
    name = df['이름']
    height = df['키']
    plt.figure(figsize=(10, 5))
    plt.ylim(150, 210)
    plt.bar(name, height, color='orange', hatch='/', ec='yellow')
    plt.xticks(name, rotation=45, size=8, color='g')
    for idx, h in enumerate(height):
        plt.text(idx, h+1, h, ha='center', color='g', size=8)

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/graph2')
def graph2(): #학생별 평균
    df['평균'] = df.apply(lambda row:row['국어':'사회'].mean(), axis=1)
    name = df['이름']
    avg = df['평균']
    plt.figure(figsize=(10, 5))
    plt.ylim(0, 100)
    plt.bar(name, avg, color='orange', hatch='/', ec='yellow')
    plt.xticks(name, rotation=45, size=8, color='g')
    for idx, h in enumerate(avg):
        plt.text(idx, h+1, f'{h:.2f}', ha='center', color='g', size=8)

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/graph3') #학교별 평균키
def graph3():
    group = df.groupby('학교')['키'].mean()
    labels = group.index
    values = group.values
    plt.figure(figsize=(10, 5))
    plt.ylim(160, 200)
    plt.bar(labels, values, color='orange', hatch='/', ec='yellow', width=0.5)
    plt.xticks(labels, rotation=45, size=8, color='g')
    for idx, value in enumerate(values):
        plt.text(idx, value+1, f'{value:.2f}cm', ha='center', color='g', size=8)

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/graph4') #학교별 평균
def graph4():
    df['평균'] = df.apply(lambda row:row['국어':'사회'].mean(), axis=1)
    group = df.groupby('학교')['평균'].mean()
    labels = group.index
    values = group.values
    plt.figure(figsize=(10, 5))
    plt.ylim(0, 100)
    plt.bar(labels, values, color='orange', hatch='/', ec='yellow', width=0.5)
    plt.xticks(labels, rotation=45, size=8, color='g')
    for idx, value in enumerate(values):
        plt.text(idx, value+1, f'{value:.2f}점', ha='center', color='g', size=8)

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/graph5') #SW특기별 인원수
def graph5():
    df['SW특기'] = df['SW특기'].str.capitalize()
    group = df.groupby('SW특기').size()
    labels = group.index
    values = group.values
    plt.figure(figsize=(10, 5))
    plt.ylim(0, 6)
    plt.bar(labels, values, color='orange', hatch='/', ec='yellow', width=0.5)
    plt.xticks(labels, rotation=45, size=10, color='g')
    for idx, value in enumerate(values):
        plt.text(idx, value+0.03, f'{value}명', ha='center', color='g', size=10)

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/')
def index():
    return render_template('index.html', title='학생관리')

if __name__=='__main__':
    app.run(port=5000, debug=True)