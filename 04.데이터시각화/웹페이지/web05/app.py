from flask import Flask, render_template, request

app = Flask(__name__, template_folder='temp')

@app.route('/')
def health():
    return render_template('health.html')

@app.route('/health/data')
def health_data():
    import pandas as pd
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