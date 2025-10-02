import requests
from bs4 import BeautifulSoup

url='https://www.naver.com/'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'lxml')
title = soup.title

print(1, title)
print(2, title.getText())

title = soup.find('title')
print(3, title)

a = soup.a
print(4, a)

span = a.span
print(5, span.getText())

attrs = a.attrs
print(6, attrs, type(attrs))

href = a['href']
print(7, href)

items = soup.find_all('a')
for item in items:
    print(item.span.getText())