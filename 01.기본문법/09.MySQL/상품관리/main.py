import os
from product import *
from sub import *

while True:
    os.system('cls')
    print('-----------------------')
    print('       상품관리          ')
    print('-----------------------')
    print('[1] 상품등록')
    print('[2] 상품검색')
    print('[3] 상품목록')
    print('[4] 상품정보수정')
    print('[5] 매출관리')
    print('[0] 프로그램종료')
    print('-----------------------')
    menu = input('메뉴선택>')
    if menu=='0':
        cur.close()
        con.close()
        print('프로그램을 종료합니다.')
        break
    elif menu=='1':
        code = inputCode('상품코드>')
        if code=='':continue
        product = read(code)
        if product != None:
            product.print()
            print('이미 등록된 상품입니다.')
        else:
            pro = Product()
            pro.code=code
            pro.name = input('상품이름>')
            pro.price = inputPrice('상품가격>')
            if pro.price == '': pro.price=0
            insert(pro)
        input('아무키나 누르세요!')
    elif menu=='2':
        while True:
            value = input('검색어>')
            if value=='': break
            products = search(value)
            if len(products)==0:
                print('검색한 상품이 없습니다!')
            else:
                for product in products:
                    product.print()
    elif menu=='3':
        products = list()
        for product in products:
            product.print()
        input('아무키나 누르세요!')
    elif menu=='4':
        code = inputCode('상품코드>')
        if code=='': continue
        pro = read(code)
        if pro==None:
            print('등록되지 않은 상품입니다.')
        else:
            name=input(f'상품이름:{pro.name}>')
            if name !='': pro.name=name
            price=inputPrice(f'상품가격:{pro.price:,}원>')
            if price !='': pro.price=price
            pro.print()
            sel = input('수정하실래요(Y)>')
            if sel=='Y' or sel=='y':
                update(pro)
            else:
                print('수정이 취소되었습니다!')
        input('아무키나 누르세요!')
    elif menu=='5':
        saleMenu()
    else:
        print('[0]~[5]번 메뉴를 선택하세요!')                                