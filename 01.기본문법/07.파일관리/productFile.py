import os
path = os.path.dirname(os.path.realpath(__file__))
file_name = path + '\product.txt'

class Product:
    def __init__(self):
        self.code=0
        self.name=''
        self.price=0
    def print(self):
        print(f'코드:{self.code}, 상품명:{self.name[:20]}, 가격:{self.price:,}원')
        print('-'*70)

#데이터 하나 추가 함수
def fileAppend(p):
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{p.code},{p.name},{p.price}\n')

#모든 데이터를 다시 쓰기 함수
def fileWrite(list):
    with open(file_name, 'w', encoding='utf-8') as file:
        for p in list:
            file.write(f'{p.code},{p.name},{p.price}\n')

#모든 데이터를 읽는 함수
def fileRead():
    with open(file_name, 'r', encoding='utf-8') as file:
        list = []
        lines = file.readlines()
        for line in lines:
            items = line.split(',')
            p = Product()
            p.code = int(items[0])
            p.name = items[1]
            p.price = int(items[2].replace('\n', ''))
            list.append(p)
        return list

def delete(code):
    list = fileRead()
    result = [p for p in list if p.code!=code]
    fileWrite(result)

def list():
    list = fileRead()
    for p in list:
        p.print()

def append():
    p = Product()
    p.code = 2
    p.name = '세탁기'
    p.price = 500
    fileAppend(p)
    print('등록성공!')

def update():
    code=1
    list = fileRead()
    result = [p for p in list if p.code==code]
    p = result[0]
    p.name='아무게'
    p.price=560
    fileWrite(list)

#list()