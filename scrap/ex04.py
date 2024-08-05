import requests
from bs4 import BeautifulSoup
import re

#쿠팡에서 노트북 검색 1페이지 데이터
url = 'https://www.coupang.com/np/search?q=노트북&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor='
headers = {
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
  "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
}
res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'lxml')
es = soup.find_all('li', attrs={'class':re.compile('^search-product')})

#애플제외, 평점수200개 이상, 평점 5.0점 이상 제품만 출력
index = 0
for e in es:
  name = e.find('div', attrs={'class':'name'}).get_text().strip()
  price = e.find('strong', attrs={'class':'price-value'}).get_text()
  if 'Apple' in name:
    continue

  count = e.find('span', attrs={'class':'rating-total-count'})
  if count:
    count = count.get_text()
  else:
    continue  
  
  count = int(count[1:-1])
  if count < 200:
    continue

  rating = e.find('em', attrs={'class':'rating'})
  if rating:
    rating = rating.get_text()
  else:
    continue  

  rating = float(rating)
  if rating < 5.0:
    continue

  index +=1
  print(index, name)
  print('가격:', price)
  print('평점수:', count)
  print('평점:', rating)
  print('-' * 80)

  