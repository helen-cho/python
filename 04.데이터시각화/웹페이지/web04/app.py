from flask import Flask, render_template, request
import pandas as pd

app =Flask(__name__, template_folder='temp')

@app.route('/score')
def score():
    return render_template('score.html')

@app.route('/score/data')
def score_data():
    word = request.args['word']
    df = pd.read_csv(f'{app.root_path}/static/score.csv')
    filt = (df['이름'].str.contains(word)) | (df['학교'].str.contains(word))
    df2 = df[filt]
    table = df2.to_html(classes='table table-striped table-hover', index=False)
    return table

if __name__=='__main__':
    app.run(port=5000, debug=True)