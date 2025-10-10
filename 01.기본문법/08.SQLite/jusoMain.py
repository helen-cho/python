from function import *
from jusoDB import *

while True:
    menuPrint('주소관리')
    menu = input('메뉴선택>')
    if menu=='0':
        print("프로그램을 종료합니다.")
        break
    elif menu=='1': #입력
        pass
    elif menu=='2': #검색
        pass
    elif menu=='3': #목록
        rows = list()
        for row in rows:
            person = Person()
            person.seq=row[0]
            person.name=row[1]
            person.address=row[2]
            person.print()
    elif menu=='4': #삭제
        pass
    elif menu=='5': #수정
        pass
    else:
        print('0~5번 숫자를 입력하세요!')                