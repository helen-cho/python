from function import *
from productFile import *

def newCode():
    list = fileRead()
    result = sorted(list, key=lambda p:p.code, reverse=True)
    if len(list)==0:
        return 1
    else:
        p=result[0]
        return p.code+1
    
while True:
    menuPrint('상품관리')
    menu = input('메뉴선택:')
    if menu=="0":
        print('프로그램을 종료합니다.')
        break
    elif menu=='1': #입력
        p = Product()
        p.code = newCode()
        print(f'상품코드>{p.code}')
        pass
    elif menu=='2': #검색
        pass
    elif menu=='3': #목록
        while True:
            sort = inputNum('1.코드순|2.이름순|3.최저가|4.최고가>')
            if sort == '':break
            list = fileRead()
            result = []
            if sort==1:result = sorted(list, key=lambda p:p.code)
            if sort==2:result = sorted(list, key=lambda p:p.name)
            if sort==3:result = sorted(list, key=lambda p:p.price)
            if sort==4:result = sorted(list, key=lambda p:p.price, reverse=True)
            print()
            for p in result:
                p.print()
    elif menu=='4': #삭제
        pass
    elif menu=='5': #수정
        pass
    else:
        print('0~5 숫자를 입력하세요!')