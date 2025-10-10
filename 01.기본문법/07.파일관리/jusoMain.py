from function import *
from jusoFile import *

def newSeq(): #새로운 번호를 리턴함수
    list = fileRead()
    if len(list)==0: return 1
    seqs = [p.seq for p in list]
    return max(seqs)+1

while True:
    menuPrint('주소관리')
    menu = input('메뉴선택>')
    if menu=="0":
        print("프로그램을 종료합니다.")
        break
    elif menu=="1": #입력
        person = Person()
        person.seq = newSeq()
        print(f"번호>{person.seq}")
        if person.seq == '': continue
        person.name = input("이름>")
        if person.name == '': continue
        person.address = input('주소>')
        fileAppend(person)
        person.print()
    elif menu=="3": #목록
        while True:
            sort = inputNum('1.최근입력순|2.이름순|3.주소순>')
            if sort == '':break
            list = fileRead()
            result = []
            if sort==1:result = sorted(list, key=lambda p:p.seq, reverse=True)
            if sort==2:result = sorted(list, key=lambda p:p.name)
            if sort==3:result = sorted(list, key=lambda p:p.address)
            for p in result:
                p.print()
            print('-' * 40)
    elif menu=="4": #삭제
        seq = inputNum("삭제번호>")
        list = fileRead()
        result = [p for p in list if p.seq==seq]
        if len(result)==0:
            print("삭제할 번호가 없습니다.")
            continue
        person = result[0]
        person.print()
        sel = input('삭제하실래요(Y)>')
        if sel == 'Y' or sel=='y':
            result = [p for p in list if p.seq!=seq]
            fileWrite(result)
            print("삭제성공!")
    elif menu=="5": #수정
        seq = inputNum('수정번호>')
        if seq == '': continue
        list = fileRead()
        result = [p for p in list if p.seq==seq]
        if len(result)==0:
            print('번호가 없습니다.')
            continue
        person = result[0]
        name = input(f'이름:{person.name}>')
        if name!='': person.name=name
        address = input(f'주소:{person.address}>')
        if address!='': person.address=address
        sel = input('수정하실래요(Y)>')
        if sel=='Y' or sel=='y':
            person.print()
            fileWrite(list)
            print('수정완료!')
    elif menu=="2": #검색
        while True:
            value = input('검색어>')
            if value=='': break
            list = fileRead()
            result=[p for p in list if p.name.find(value)!=-1 or p.address.find(value)!=-1]
            if len(result)==0:
                print('검색내용이 없습니다.')
                continue
            for person in result:
                person.print()
