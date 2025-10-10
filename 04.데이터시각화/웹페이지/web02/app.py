from flask import Flask, render_template, send_file
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.rc('axes', unicode_minus=False)

import pandas as pd
df = pd.read_csv('c:/python/04.데이터시각화/data/score.csv')

from io import BytesIO

app = Flask(__name__, template_folder='temp')

@app.route('/')
def index():
    return render_template('index.html', title='그래프연습')

@app.route('/graph4')
def graph4():
    df['학년'] = [3,3,2,1,1,3,2,2]
    plt.scatter(df['국어'], df['영어'], sizes=df['학년']*500, c=df['학년'], alpha=0.3)
    plt.colorbar(ticks=[1, 2, 3], orientation='horizontal', label='학년', shrink=0.5)
    for idx in range(len(df)):
        x = df.loc[idx, '국어']
        y = df.loc[idx, '영어']
        name = df.loc[idx, '이름']
        plt.text(x, y, name, ha='center', size=8)
    plt.ylim(0, 120)
    #plt.show()

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/graph3')
def graph3():
    group = df.groupby('SW특기').size()
    plt.pie(group.values, explode=[0.05] * len(group), 
            wedgeprops={'width':0.8, 'alpha':0.3},
            labels=group.index, autopct='%.1f%%')
    
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/graph2')
def graph2():
    x = df.index * 4
    plt.figure(figsize=(10, 5))
    plt.bar(x, df['국어'], width=1, label='국어')
    plt.bar(x+1, df['영어'], width=1, label='영어')
    plt.bar(x+2, df['수학'], width=1, label='수학')
    plt.legend()
    xticks = [xtick+1 for xtick in x]
    plt.xticks(xticks, df['이름'])
    #plt.show()

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/graph1')
def graph1():
    plt.figure(figsize=(10, 5))
    plt.bar(df['이름'], df['국어'], label='국어')
    plt.bar(df['이름'], df['영어'], bottom=df['국어'], label='영어')
    plt.bar(df['이름'], df['수학'], bottom=df['국어']+df['영어'], label='수학')
    plt.ylim(0, 300)
    plt.legend()
    #plt.show()

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/score')
def score():
    table = df.to_html(classes='table table-striped')
    return render_template(
        'page1.html',
        table1= table)

if __name__=='__main__':
    app.run(port=5000, debug=True)