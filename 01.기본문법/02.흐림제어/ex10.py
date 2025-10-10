address = [
    {'no':3, 'name':'이순신', 'juso':'인천 서구 경서동'},
    {'no':4, 'name':'심청이', 'juso':'경기도 광명시 철산동'},
]
while True:
    print('\n*************주소관리 프로그램**************')
    print('-' * 45)
    print('|1.입력|2.목록|3.검색|4.삭제|5.수정|0.종료|')
    print('-' * 45)
    menu = input('메뉴선택>')
    if menu == '0':
        print('프로그램을 종료합니다.')
        break
    elif menu=='1':
        #입력시작------------------------------------------------
        no = []
        for a in address:
            no.append(a['no'])
        new_no = max(no)+1
        print(f'번호>{new_no}')
        name = input('이름>')
        juso = input('주소>')
        address.append({'no':new_no, 'name':name, 'juso':juso})
        print('새로운 주소가 등록되었습니다.')
        #입력종료------------------------------------------------
        pass
    elif menu=='2':
        #목록시작------------------------------------------------
        for a in address:
            print(a['no'], a['name'], a['juso'])
        #목록종료------------------------------------------------
    elif menu=='3':
        #검색시작------------------------------------------------
        name=input('검색이름>')
        for a in address:
            if a['name'].find(name) != -1:
                print(a['no'], a['name'], a['juso'])
        #검색종료------------------------------------------------
    elif menu=='4':
        #삭제시작------------------------------------------------
        no = input('삭제번호>')
        if no == '':
            continue
        for index, a  in enumerate(address):
            if int(no)==a['no']:
                address.pop(index)
                print(no, '번 삭제되었습니다.')
        #삭제종료------------------------------------------------
    elif menu=='5':
        #수정시작------------------------------------------------
        no = input('수정번호>')
        for a in address:
            if int(no)==a['no']: #수정번호를 찾은경우
                name = input(f'이름:{a["name"]}>')
                if name != '': #수정할 경우
                    a['name'] = name
                juso = input(f'주소:{a["juso"]}>')
                if juso != '':
                    a['juso'] = juso    
        #수정종료------------------------------------------------
    else:
        print('0~5번을 다시 선택하세요!')