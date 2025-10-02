import requests
from bs4 import BeautifulSoup

def weather(city):
    city = city + '날씨'
    url=f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={city}&ackey=bxgioco6'
    res = requests.get(url)
    #print(res)
    soup = BeautifulSoup(res.text, 'lxml')

    summary = soup.find('p', attrs={'class':'summary'}).getText()
    #print(summary)

    #현재온도
    temp = soup.find('div', attrs={'class':'temperature_text'}).strong.contents[1]
    #print(temp)

    #최저온도
    lowest = soup.find('span', attrs={'class':'lowest'}).contents[1].replace('°','')
    #print(lowest)

    #최고온도
    highest = soup.find('span', attrs={'class':'highest'}).contents[1].replace('°','')
    #print(highest)


    print('[오늘날씨]')
    print('-' * 50)
    print(summary)
    print(f'현재온도: {temp}도 (최저:{lowest}도 / 최고:{highest}도)')
    print('-' * 50)

if __name__=='__main__':
    while True:
        city = input('지역명>')
        if city=='': break
        weather(city)