from flask import Flask, render_template
import pandas as pd

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
  return "hello"

@app.route('/wine/list.json')
def wineList():
  df = pd.read_csv('data/wineInfo_RedV2.csv')
  #data = df.iloc[:10]
  return df.to_json(orient='records')

if __name__ == '__main__':
  app.run(port=5000, debug=True, host='192.168.0.98')