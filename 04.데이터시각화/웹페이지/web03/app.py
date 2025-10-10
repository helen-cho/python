from flask import Flask, render_template, request
import pandas as pd

df = pd.read_csv('c:/python/04.데이터시각화/data/score.csv')

app = Flask(__name__, template_folder='temp')

@app.route('/')
def index():
    if not request.args['word']: word=''
    #word='황'
    filt = df['이름'].str.contains(word)
    df3 = df
    df1 = df3[['지원번호', '이름', '학교', '키', 'SW특기']]
    df2 = df3[['지원번호', '이름', '국어', '영어', '수학', '과학', '사회']]

    info = df1.to_html(classes='table table-striped table-hover', index=False)
    score = df2.to_html(classes='table table-striped table-hover', index=False)

    return render_template('index.html', info=info, score=score)

if __name__=='__main__':
    app.run(port=5000, debug=True)