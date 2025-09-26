import os
from sale import *
from product import *

def saleMenu():
    while True:
        os.system('cls')
        print('-----------------------')
        print('       매출관리          ')
        print('-----------------------')
        print('[1] 매출등록')
        print('[2] 매출검색')
        print('[3] 매출목록')
        print('[4] 매출정보수정')
        print('[5] 매출삭제')
        print('[0] 상품관리')
        print('-----------------------')
        menu = input('메뉴선택>')
        if menu=='0':
            break
        elif menu=='1':
            code = inputCode('상품코드>')
            pro = read(code)
            if pro==None:
                print('등록된 상품이 없습니다.')
            else:
                pro.print()
                sale = Sale()
                sale.code=code
                price = inputPrice(f'판매가격{pro.price:,}원>')
                if price == '' : 
                    sale.price=pro.price
                else:
                    sale.price=price
                qnt = inputNum('판매수량>')
                if qnt=='': qnt=0
                sale.qnt = qnt
                print(f'상품코드:{sale.code}, 판매가격:{sale.price}, 판매수량:{sale.qnt}')
                sale_insert(sale)
            input('아무키나 누르세요!')
        elif menu=='2':
            while True:
                value = input('검색어>')
                if value=='':break
                sales = sale_list(value)
                for sale in sales:
                    sale.print()
        elif menu=='3':
            sales = sale_list('')
            for sale in sales:
                sale.print()
            input('아무키나 누르세요!')
        elif menu=='4':
            input('아무키나 누르세요!')
        elif menu=='5':
            input('아무키나 누르세요!')
        else:
            print('[0]~[5] 메뉴를 선택하세요!')
            input('아무키나 누르세요!')

if __name__=='__main__':
    saleMenu()