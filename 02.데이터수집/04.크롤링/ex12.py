from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re, time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
#options.add_argument('headless')

browser = webdriver.Chrome(options=options)
browser.maximize_window()
keyword='자바'
url=f'https://www.hanbit.co.kr/search/search_list.html?keyword={keyword}'
browser.get(url)

#더보기
es = browser.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div[2]/h2')
es.click()
time.sleep(2)

soup = BeautifulSoup(browser.page_source, 'lxml')
books = soup.find('div', {'class':'ser_list_wrap'})
books = books.find_all('li', {'class':'ser_bg'})

list = []
for book in books:
    no = len(list) + 1
    title=book.strong.getText()
    image=book.img['src']
    author=book.span.getText()
    link = 'https://www.hanbit.co.kr/' + book.a['href']
    print(title, image, author, link)
    data ={'no':no, 'title':title, 'image':image, 'author':author, 'link':link}
    list.append(data)

import json
#json 파일에 저장
with open('data/books.json', 'a', encoding='utf-8') as file:
    json.dump(list, file, indent='\t', ensure_ascii=False)

print('프로그램종료!')