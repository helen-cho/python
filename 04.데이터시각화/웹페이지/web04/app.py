from flask import Flask, render_template, request, send_file
import pandas as pd

app =Flask(__name__, template_folder='temp')

@app.route('/score')
def score():
    return render_template('score.html')

@app.route('/score/graph')
def score_graph():
    import matplotlib.pyplot as plt
    from io import BytesIO

    plt.rc('font', family='Malgun Gothic')
    plt.rc('axes', unicode_minus=False)
    
    df = pd.read_csv(f'{app.root_path}/static/score.csv')
    df['평균'] = df.apply(lambda row:row['국어':'사회'].mean(), axis=1)
    plt.bar(df['이름'], df['평균'])

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/score/data')
def score_data():
    word = request.args['word']
    df = pd.read_csv(f'{app.root_path}/static/score.csv')

    df['평균'] = df.apply(lambda row:row['국어':'사회'].mean(), axis=1)
    filt = (df['이름'].str.contains(word)) | (df['학교'].str.contains(word))
    df = df[filt]

    df_info = df[['지원번호', '이름', '학교', '키', 'SW특기']]
    df_score = df[['지원번호', '이름', '국어','영어','수학', '과학', '사회', '평균']]

    table_info = df_info.to_html(classes='table table-striped table-hover', index=False)
    table_score = df_score.to_html(classes='table table-striped table-hover', index=False)
    data = {'info':table_info, 'score':table_score}
    return data

if __name__=='__main__':
    app.run(port=5000, debug=True)