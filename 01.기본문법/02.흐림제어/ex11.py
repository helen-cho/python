product = [
    {'code':1, 'name':'엘지 냉장고', 'price':2500000},
    {'code':2, 'name':'삼성 세탁기', 'price':1800000},
    {'code':3, 'name':'삼성 냉장고', 'price':2100000},
    {'code':4, 'name':'엘지 전자동 세탁기', 'price':2000000},
]

while True:
    print('\n*************상품관리 프로그램**************')
    print('-' * 45)
    print('|1.입력|2.목록|3.검색|4.삭제|5.수정|0.종료|')
    print('-' * 45)
    menu = input('메뉴선택>')
    if menu == '0':
        print('프로그램을 종료합니다.')
        break
    elif menu=='2':
        for p in product:
            print(p['code'], p['name'], f"{p['price']:,}원")
    elif menu=='4':
        del_code = input('삭제코드>')
        if not del_code.isnumeric():
            print('삭제코드는 숫자입니다.')
            continue
        for index, p in enumerate(product):
            if int(del_code)==p['code']:
                product.pop(index)
                print(f'{p["name"]} 상품이 삭제되었습니다.')
    elif menu=='1':
        codes = []
        for p in product:
            codes.append(p['code'])
        new_code = max(codes)+1
        print(f'상품코드>{new_code}')
        new_name = input('상품이름>')
        new_price = int(input('상품가격>'))
        product.append({'code':new_code, 'name':new_name, 'price':new_price})
        print('새로운 상품이 등록되었습니다.')
    elif menu=='3':
        search_name = input('상품이름>')
        for p in product:
            if p['name'].find(search_name) != -1:
                print(p['code'], p['name'], f"{p['price']:,}원")
    elif menu=='5':
        edit_code =input('수정코드>')
        for p in product:
            if int(edit_code)==p['code']:
                #상품명 수정
                new_name=input(f'상품명:{p["name"]}>')
                if new_name != '':
                    p['name']=new_name
                #상품가격 수정    
                new_price=input(f"가격:{p['price']:,}>")
                if new_price != '':
                    p['price'] = int(new_price)