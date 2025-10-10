#도서검색
import requests
import os

def getBooks(url, query, page, size):
    try:
        headers={'Authorization':'KakaoAK 4a8e1acc493134e630bb6e1dd8deb6eb'}
        url = f'{url}?query={query}&page={page}&size={size}'
        res = requests.request(method='get', url=url, headers=headers)
        data = res.json()
        documents = data['documents']
        if len(documents)==0:
            print('검색 도서가 없습니다.')
        for doc in documents:
            title = doc['title']
            price = doc['sale_price']
            authors = doc['authors']
            publisher=doc['publisher']
            print(title, price, ','.join(authors), publisher)
    except Exception as err:
        print('접속오류:', err)


if __name__=='__main__':
    url='https://dapi.kakao.com/v3/search/book'
    page=1
    size=10

    os.system('cls')
    while True:
        print()
        query = input('검색도서명>')
        if query=='': break
        getBooks(url, query, page, size)