import requests
from bs4 import BeautifulSoup

def create_soup(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    return soup


def scrap(section):
    url=f'https://news.naver.com/section/{section}'
    soup = create_soup(url)
    news = soup.find('ul', attrs={'class':'sa_list'})
    li = news.find_all('li', limit=5)
    for idx, item in enumerate(li):
        title = item.find('strong', attrs={'class':'sa_text_strong'}).getText()
        link = item.find('a')['href']
        print(idx+1, title)
        print(link)

if __name__=='__main__':
    while True:
        section = input('\n경제:101|사회:102|생활/문화:103>')
        if section=='': break
        scrap(section)