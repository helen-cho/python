import requests
from bs4 import BeautifulSoup
import csv
import re

file_name ='data/시가총액1~200.csv'
file = open(file_name, 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(file)
title='N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론'
title = title.split('\t')
writer.writerow(title)

#[시가총액 순위]-[더보기]-[코스피] 1~200
for page in range(1, 5):
    url=f'https://finance.naver.com/sise/sise_market_sum.naver?&page={page}'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')

    table = soup.find('table', attrs={'class':'type_2'})
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        if len(cols) <=1: continue
        data=[re.sub('\t|\n|상승|하락|보합', '',col.getText()) for col in cols]
        writer.writerow(data)