import requests
from bs4 import BeautifulSoup
import time, re

def create_soup(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    return soup

def answer(input_text):
    answer_text = ''
    if '안녕' in input_text:
        time.sleep(1)
        answer_text = '안녕하세요? 반갑습니다.'
    elif '날씨' in input_text:
        temp = weather(input_text)
        answer_text = '오늘의 ' + temp.strip() + '입니다.'
    elif '환율' in input_text:
        rate = exchange()
        answer_text = '1달러 환율은 ' + rate + '입니다.'
    elif '주식' in input_text:
        price = stock(input_text)
        answer_text = '1주는 ' + price + '원 입니다.'
    elif '고마워' in input_text:
        time.sleep(1)
        answer_text = '별말씀을요.'
    else:
        time.sleep(1)
        answer_text = '다시 한번 말씀해 주시겠어요?'
    return answer_text

def weather(query):
    url=f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={query}'
    soup = create_soup(url)
    temp = soup.find('div', attrs={'class':'temperature_text'})
    if temp:
        temp = temp.getText()
    else:
        temp = ''
    return temp

def exchange():
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=환율'
    soup = create_soup(url)
    rate = soup.find('span', attrs={'class': re.compile('^spt_con')}).find('strong')
    if rate:
        rate = rate.getText()
    else:
        rate = ''
    return rate

def stock(query):
    url=f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={query}'
    soup = create_soup(url)
    price = soup.find('div', attrs={'class':re.compile('^spt_con')}).find('strong')
    if price:
        price = price.getText()
    else:
        price = ''
    return price

if __name__=='__main__':
    text = answer('카카오주식')
    print(text)