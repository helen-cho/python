from flask import Flask, render_template, request, send_file
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

plt.rc('font', family = 'Malgun Gothic')
plt.rc('axes', unicode_minus = False)

app = Flask(__name__, template_folder='temp')

@app.route('/')
def health():
    return render_template('health.html')

@app.route('/health/graph')
def health_graph():
    plt.rc('font', size=6)
    df = pd.read_csv(f'{app.root_path}/data/인구수별공공의료기관수.csv')
    word=request.args['word']
    filt = df['시도군구'].str.contains(word)
    df = df[filt]
    if len(df)>0:
        df = df[:10]

    plt.title('지역별 공공의료기관 수', size=20)
    plt.barh(df['시도군구'], df['count'])

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/health/data')
def health_data():
    page = int(request.args['page'])
    size = int(request.args['size'])
    word = request.args['word']

    df = pd.read_csv(f'{app.root_path}/data/인구수별공공의료기관수.csv')
    filt = df['시도군구'].str.contains(word)
    df = df[filt]

    start = (page-1) * size
    end = page * size
    df2 = df[start:end]
    count = len(df)
    table = df2.to_html(index=True, classes='table table-striped table-hover')

    data = {'count':count, 'table':table}
    return data

if __name__=='__main__':
    app.run(port=5000, debug=True)