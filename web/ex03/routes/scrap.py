from flask import Blueprint, render_template

bp = Blueprint('scrap', __name__, url_prefix='/scrap')

#무비챠트 Scrapping
def scrap_movie():
  import requests
  from bs4 import BeautifulSoup
  import json

  url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
  res = requests.get(url)
  soup = BeautifulSoup(res.text, 'lxml')
  es = soup.find('div', attrs={'class':'sect-movie-chart'}).find_all('li', limit=12)
  items = []
  for e in es:
    rank = e.find('strong', attrs={'class':'rank'}).get_text()
    title = e.find('strong', attrs={'class':'title'}).get_text()
    image = e.find('img')['src']
    date = e.find('span', attrs={'class':'txt-info'}).get_text().strip()[0:10]
    link=e.find('a', attrs={'class':'link-reservation'})['href']
    link='http://www.cgv.co.kr' + link
    data ={'rank':rank, 'title':title, 'image':image, 'date':date, 'link':link}
    items.append(data)
  
  with open('static/data/movie.json', 'w', encoding='utf8') as file:
    json.dump(items, file, indent='\t', ensure_ascii=False)

  return items

@bp.route('/movie')
def movie():
  return render_template('index.html', title='무비챠트', pageName='scrap/movie.html')

@bp.route('/movie.json')
def movie_json():
  import json
  import os
  if os.path.isfile('static/data/movie.json'):
    with open('static/data/movie.json', 'r', encoding='utf8') as file:
      json_data = json.load(file)
  else:
    json_data = scrap_movie()
  return json_data

@bp.route('/finance')
def finance():
  return render_template('index.html', 
                         title='시가총액', pageName='scrap/finance.html')

@bp.route('/finance.json')
def scrap_finace():
  #CSV -> JSON 변환
  import csv
  import json
  data = []
  with open('static/data/코스피시가총액1~100.csv', 'r', encoding='utf-8') as csv_file:
    reader =  csv.DictReader(csv_file)
    data = list(reader)
  
  json_data = json.dumps(data, indent=4, ensure_ascii=False)
  return json_data