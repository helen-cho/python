import os
path = os.path.dirname(os.path.realpath(__file__))
#print('현재패스:', path)

#주소 관리 클래스
class Person:
    def __init__(self): #생성자
        self.seq = 0 #속성(seq, name, address)
        self.name=''
        self.address='경기도 광명시'

    def print(self): #메서드
        #print('번호:' + self.seq + ' ,이름:' + self.name)
        print(f'번호:{self.seq}, 이름:{self.name}, 주소:{self.address}')

file_name = path + '/juso.txt'

#파일에 객체를 추가하는 함수
def fileAppend(person):
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{person.seq},{person.name},{person.address}\n')

#파일에 객체를 추가하는 함수
def fileWrite(list):
    with open(file_name, 'w', encoding='utf-8') as file:
        for person in list:
            file.write(f'{person.seq},{person.name},{person.address}\n')

#파일에서 데이틀 읽어오는 함수
def fileRead():
    list = []
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            items = line.split(',')
            person = Person()
            person.seq = int(items[0])
            person.name = items[1]
            person.address = items[2].replace('\n', '')
            list.append(person)
        return list    
    
#목록 출력 테스트
def list():
    list = fileRead()
    for person in list:
        person.print()

#데이터 추가 테스트 
def append():
    person = Person()
    person.seq=1
    person.name='이순신'
    person.address='인천 서구 경서동'
    person.print()
    fileAppend(person)
    print('입력성공!')

def search(type, value):
    list = fileRead()
    result = []
    if type==1: #seq 검색
        result = [person for person in list if person.seq==value]
    elif type==2: #name 검색
        result = [person for person in list if person.name.find(value)!=-1]
    elif type==3: #address 검색
        result = [person for person in list if person.address.find(value)!=-1]    
    return result

#삭제 함수
def delete(seq):
    list = fileRead()
    result = [person for person in list if person.seq==seq]
    if len(result)==0:
        print("검색결과가 없습니다.")
    else:
        result = [person for person in list if person.seq != seq]
        fileWrite(result)
        print('삭제성공!')

#수정 함수
def update(seq):
    list = fileRead()
    result = [person for person in list if person.seq==seq]
    if len(result)==0:
        print("검색결과가 없습니다.")
    else:    
        person = result[0]
        name = input(f'이름:{person.name}>')
        if name != '': person.name = name
        address = input(f'주소:{person.address}>')
        if address !='': person.address= address
        fileWrite(list)
        person.print()
        print('수정완료!')

if __name__=='__main__':
    update(3)