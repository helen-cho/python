from function import *

file_name = 'C:/python/01.기본문법/data/juso.txt'
#파일에 데이터저장
def insert(name, phone, address):
    with open(file_name, 'a', encoding='utf-8') as file:
        no = maxNo() + 1
        file.write(f"{no},{name},{phone},{address}\n")
        print("등록완료!")

#파일에 데이터를 읽어서 list 리턴하는 함수
def read():
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        list = [] #데이터를 저장
        for line in lines:
            items = line.split(",")
            no = items[0]
            name = items[1]
            phone= items[2]
            address=items[3]
            item = {'no':no, 'name':name, 'phone':phone, 'address':address}
            list.append(item) #item을 list에 추가
        return list

#이름을 받아서 검색결과를 딕션러리로 리턴하는 함수
def search(name):
    items = read()
    list = []
    for item in items:
        if item['name'].find(name) != -1:
            list.append(item)
    return list

#가장큰 번호를 찾아서 리턴하는 함수
def maxNo():
    items = read()
    nos = []
    for item in items:
        nos.append(int(item['no']))
    if len(nos)==0:
        return 0
    else:
        return max(nos)

while True:
    menuPrint("주소관리")
    menu = input("메뉴선택>")
    if menu=="0":
        break
    elif menu=="1": #입력
        name = input("이름>")
        if name=="": continue
        phone = input("전화>")
        address = input("주소>")
        insert(name, phone, address)
    elif menu=="3": #목록
        items = read()
        for item in items:
            print(f"{item['no']},{item['name']},{item['phone']},{item['address']}", end="")
    elif menu=="2": #검색
        name = input("검색이름>")
        list = search(name)
        if len(list)==0:
            print(f"'{name}' 데이터가 없습니다.")
            continue
        for item in list:
            print(f"{item['no']},{item['name']},{item['phone']},{item['address']}",end="")
