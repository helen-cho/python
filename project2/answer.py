import requests
from bs4 import BeautifulSoup
import time

def create_soup(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    return soup


def weather():
    url='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98%EB%82%A0%EC%94%A8&ackey=xhv7y3jw'
    soup = create_soup(url)
    temp = soup.find('div', attrs={'class':'temperature_text'})
    if temp:
        temp = temp.getText()
    else:
        temp = ''
    return temp

if __name__=='__main__':
    temp=weather()
    print(temp)