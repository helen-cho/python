import requests
from bs4 import BeautifulSoup
import re

def create_soup(query, page):
  url="https://www.coupang.com/np/search?q={}&channel=user\
    &component=&eventCategory=SRP&trcid=\
    &traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=\
    &filterType=&listSize=36&filter=&isPriceRange=false&brand=\
    &offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=\
    &backgroundColor=".format(query, page)
  headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
  }
  res = requests.get(url, headers=headers)
  soup = BeautifulSoup(res.text, "lxml")
  return soup

index=0
items=[]
for i in range(1, 6):
  soup = create_soup('노트북', i)
  es = soup.find_all('li', attrs={'class':re.compile('^search-product')})
  for e in es:
    name = e.find('div', attrs={'class':'name'})
    if name:
      name = name.get_text().strip()
    else:
      continue
    price = e.find('strong', attrs={'class':'price-value'})
    if price:
      price = price.get_text()
    else:
      continue
    image = e.find('img', attrs={'class':'search-product-wrap-img'})
    if image:
      image = 'https:' + image['src']
    else:
      continue
    index +=1
    print(index, name)  
    print("가격:", price)
    print("이미지:", image)

    item = {'name':name, 'price':price, 'image':image}
    items.append(item)

    #이미지 다운로드
    # res_image = requests.get(image)
    # with open('images/img{}.jpg'.format(index), 'wb') as file:
    #   file.write(res_image.content)

#items JSON 파일로 저장
import json
with open('data/shop.json', 'w', encoding='utf-8') as file:
  file.write(json.dumps(items, indent=4, sort_keys=True, ensure_ascii=False))

print('상품수:', index)
