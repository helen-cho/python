#검색함수 (list와 code를 입력받아서 list에서 code를 검색)
def search(list, code):
    for index, item in enumerate(list):
        if item['code']==code:
            return index
        

sale = [
    {'code':1, 'name':'냉장고', 'price':250, 'qnt':5},
    {'code':2, 'name':'세탁기', 'price':150, 'qnt':3},
]

index = search(sale, 2)
if index == None:
    print("해당데이터가 없습니다.")
else:
    print(sale[index])    