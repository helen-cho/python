import os
from db import *

def menuDept():
    os.system('cls')
    while True:
        print()
        print('*********학과관리*************')
        print('-----------------------------')
        print('1.등록|2.목록|3.수정|0.종료')
        print('-----------------------------')
        menu = input('메뉴선택>')
        if menu=='0':
            break
        elif menu=='3':
            dcode = inputCode('학과코드>', 5)
            dept = readDept(dcode)
            dname = input(f'학과이름:{dept.dname}>')
            if dname!='': dept.dname=dname
            updateDept(dept)

        elif menu=='1':
            dname = input('학과이름>')
            if dname=='':continue
            insertDept(dname)
        elif menu=='2':
            list = listDept()
            for dept in list:
                print(f'학과코드:{dept.dcode}, 학과이름:{dept.dname}')