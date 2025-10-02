jusos = [
    {'no':1, 'name':'홍길동', 'juso':'서울 강서구'},
    {'no':2, 'name':'강감찬', 'juso':'인천 서구'},
]
while True:
    print()
    print('-' * 35)
    print('******** 주소관리프로그램 *********')
    print('-' * 35)
    print('|1.입력|2.검색|3.수정|4.삭제|0.종료')
    print('-' * 35)
    menu = input('메뉴선택>')
    if menu == '0':
        print('프로그램을 종료합니다.')
        break
    elif menu == '1': #입력
        no = input('번호>')
        name = input('이름>')
        juso = input('주소>')
        jusos.append({'no':no, 'name':name, 'juso':juso})
        print('등록완료!')
    elif menu == '2': #검색
        for j in jusos:
            print(j.get('no'), j.get('name'), j['juso'])
        print('-' * 50)    
        print(len(jusos), '명이 존재합니다.')
    elif menu == '3': #수정
        pass
    elif menu == '4': #삭제
        pass
    else:
        print('메뉴를 0~4를 입력하세요!')