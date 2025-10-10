import pymysql

con = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    db='haksa',
    charset='utf8',
    port=3306,
    cursorclass=pymysql.cursors.DictCursor)
cur = con.cursor()

class Dept:
    def __init__(self):
        self.dcode = 0
        self.dname = ''

class Student(Dept):
    def __init__(self):
        super().__init__()
        self.id = ''
        self.name = ''
        self.code = 0
    def print(self):
        print(f'학번:{self.id}, 이름:{self.name}, 학과:{self.dname}({self.code})')
        print('-' * 50)    

def list(key):
    try:
        keys=['id', 'name', 'dname']
        sql = f'select * from vstudent order by {keys[key-1]}'         
        cur.execute(sql)
        rows = cur.fetchall()
        list = []
        for row in rows:
            stu = Student()
            stu.id = row['id']
            stu.name = row['name']
            stu.dname = row['dname']
            stu.code = row['code']
            list.append(stu)
        return list
    except Exception as err:
        print('학생목록오류:', err)

def search(value):
    try:
        sql = 'select * from vstudent where id like %s or name like %s or dname like %s'
        value = f'%{value}%'
        cur.execute(sql, (value, value, value))
        rows = cur.fetchall()
        if not rows==None:
            list = []
            for row in rows:
                stu = Student()
                stu.id = row['id']
                stu.name = row['name']
                stu.code = row['code']
                stu.dname = row['dname']
                list.append(stu)
            return list
    except Exception as err:
        print('학생검색오류:', err)

def newID():
    try:
        sql = 'select convert(max(id)+1, char(4)) as new_id from student'
        cur.execute(sql)
        row = cur.fetchone()
        return row['new_id']
    except Exception as err:
        print('새로운학번:', err)

def listDept():
    try:
        sql = 'select * from dept'
        cur.execute(sql)
        rows = cur.fetchall()
        list = []
        for row in rows:
            dept = Dept()
            dept.dcode = row['dcode']
            dept.dname = row['dname']
            list.append(dept)
        return list
    except Exception as err:
        print('학과목록:', err)

#학과코드입력함수
def inputCode(title, menu):
    list = listDept()
    codes = [dept.dcode for dept in list]
    print('-' * 50)
    for dept in list:
        print(f'{dept.dcode}.{dept.dname}', end='|')
    print()
    print('-' * 50)
    while True:
        code = input(title)
        if code=='' and menu==1:
            print('학과코드는 꼭 입력하세요!')
        elif code=='' and menu==5:
            return code    
        elif not code.isnumeric():
            print('학과는 숫자로 입력하세요!')
        elif codes.count(int(code))==0:
            print(f'{codes} 코드번호를 입력하세요!')
        else:
            return int(code)        

def insert(stu):
    try:
        sql = 'insert into student(id, name, code) values(%s, %s, %s)'
        cur.execute(sql, (stu.id, stu.name, stu.code))
        con.commit()
        print('학생등록완료!')
    except Exception as err:
        print('학생등록오류:', err)

def read(id):
    try:
        sql = 'select * from vstudent where id=%s'
        cur.execute(sql, (id))
        row = cur.fetchone()
        if row!=None:
            stu = Student()
            stu.id = row['id']
            stu.name = row['name']
            stu.code = row['code']
            stu.dname = row['dname']
            return stu
    except Exception as err:
        print('학생읽기오류:', err)

def delete(id):
    try:
        sql = 'delete from student where id=%s'
        cur.execute(sql, (id))
        con.commit()
        print('학생삭제완료!')
    except Exception as err:
        print('학생삭제오류:',err)

def update(stu):
    try:
        sql = 'update student set name=%s, code=%s where id=%s'
        cur.execute(sql, (stu.name, stu.code, stu.id))
        con.commit()
        print('학생수정완료!')
    except Exception as err:
        print('학생수정오류:', err)

#학과등록
def insertDept(dname):
    sql = 'insert into dept(dname) values(%s)'
    cur.execute(sql, (dname))
    con.commit()
    print('학과등록완료!')

#학과읽기
def readDept(dcode):
    sql = 'select * from dept where dcode=%s'
    cur.execute(sql, (dcode))
    row = cur.fetchone()
    dept = Dept()
    dept.dcode = row['dcode']
    dept.dname = row['dname']
    return dept

#학과수정
def updateDept(dept):
    sql = 'update dept set dname=%s where dcode=%s'
    cur.execute(sql, (dept.dname, dept.dcode))
    con.commit()
    print('학과수정완료!')

if __name__=='__main__':
    id = input('학번>')
    stu = read(id)
    if stu==None:
        print('학생이 없습니다.')
    else:
        stu.print()

        
        