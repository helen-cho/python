import requests
import csv
from bs4 import BeautifulSoup
import re

file_name ='data/코스닥거래상위1~100.csv'
file = open(file_name, 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(file)

#[Top종목]-[거래상위]-[더보기]-[코스닥]
url='https://finance.naver.com/sise/sise_quant.naver?sosok=1'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

table = soup.find('table', attrs={'class':'type_2'})
rows = table.find_all('tr')


for row in rows:
    cols = row.find_all('td')
    if len(cols) <=1 :continue
    data = [re.sub('\t|\n|상승|하락|보합','', col.getText()) for col in cols]
    print(data)
    break
    writer.writerow(data)