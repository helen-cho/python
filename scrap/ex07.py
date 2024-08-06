import requests
from bs4 import BeautifulSoup
import re
import csv

url='https://finance.naver.com/sise/sise_quant.naver'
res = requests.get(url)

soup = BeautifulSoup(res.text, "lxml")
es = soup.find("table", attrs={'class':'type_2'}).find_all('tr')

file = open('data/코스피거래상위1~100.csv', 'w', encoding='utf-8-sig', newline="")
writer = csv.writer(file)
title='N	종목명	현재가	전일비	등락률	거래량	거래대금	매수호가	매도호가	시가총액	PER	ROE'.split('\t')
writer.writerow(title)

for e in es:
  columns = e.find_all("td")
  if len(columns) <= 1:
    continue

  # data = []
  # for col in columns:
  #   col = col.get_text()
  #   col = re.sub('\n|\t|상승|하락|보합','', col)
  #   data.append(col)

  data = [re.sub('\n|\t|상승|하락|보합','', col.get_text()) for col in columns] 
  writer.writerow(data) 
  print(data)