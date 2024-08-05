import requests
from bs4 import BeautifulSoup

#CGV 무비챠트
url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'lxml')

movie = soup.find('div', attrs={'class':'sect-movie-chart'})
movies = movie.find_all('li')
#print(len(movies))
for index, m in enumerate(movies):
  title = m.find('strong', attrs={'class':'title'}).get_text()
  img = m.find('img').attrs['src']
  link = m.find('a', attrs={'class':'link-reservation'})['href']
  date = m.find('span', attrs={'class':'txt-info'}).find('strong').get_text().strip()
  percent = m.find('strong', attrs={'class':'percent'}).find('span').get_text()
  print(str(index+1), title)
  print(img)
  print('개봉일:', date[0:10])
  print('http://www.cgv.co.kr' + link)
  print('예매율:', percent)
  print('-' * 80)

