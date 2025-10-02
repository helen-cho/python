from function import *
from productDB import *

while True:
    menuPrint('상품관리')
    menu = input('메뉴선택>')
    if menu=='0':
        print("프로그램을 종료합니다.")
        break
    elif menu=='1':
        p = Product()
        p.name = input('상품이름>')
        if p.name=='': continue
        p.price = inputNum('상품가격>')
        if p.price=='': p.price=0
        insert(p)
        print('상품등록완료!')
    elif menu=='2':
        while True:
            value = input('검색어>')
            if value=='':break
            rows = search(value)
            for row in rows:
                rowPrint(row)
    elif menu=='3':
        while True:
            type=inputNum('1.코드순|2.상품이름순|3.최저가|4.최고가>')
            if type=='':break
            rows = list(type)
            for row in rows:
                rowPrint(row)
    elif menu=='4':
        code = inputNum('상품코드>')
        if code=='': continue
        row = read(code)
        p = rowPrint(row)
        sel=input('삭제하실래요(Y)>')
        if sel=='Y' or sel=='y':
            delete(code)
            print('상품삭제완료!')
    elif menu=='5':
        code = inputNum('상품코드>')
        if code=='': continue
        row = read(code)
        if row==None:
            print('해당상품이 없습니다.')
            continue
        p = rowPrint2(row)
        name = input(f'상품이름:{p.name}>')
        if name!='': p.name=name
        price = input(f'상품가격:{p.price:,}원>')
        if price!='': p.price=price
        sel=input('수정하실래요(Y)>')
        if sel=='Y' or sel=='y':
            update(p)
            print('상품수정완료!')        