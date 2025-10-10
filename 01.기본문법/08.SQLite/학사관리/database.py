from function import *
import os, sqlite3
path = os.path.dirname(os.path.realpath(__file__))
db_name = path + '/haksa.db'

con = sqlite3.connect(db_name)
cur = con.cursor()

class Dept:
    def __init__(self):
        self.code=0
        self.dname=''

class Student(Dept):
    def __init__(self):
        super().__init__()
        self.id = ''
        self.name = ''
        self.dept=0

    def print(self):
        print(f'학번:{self.id}, 이름:{self.name}, 학과:{self.dname}({self.dept})')



def list():
    try:
        sql = 'select * from vstudent'
        cur.execute(sql)
        rows = cur.fetchall()
        list=[]
        for row in rows:
            stu = Student()
            stu.id = row[0]
            stu.dept = row[1]
            stu.name = row[2]
            stu.dname = row[3]
            list.append(stu)
        return list
    except Exception as err:
        print('목록 에러:', err)
    finally:
        pass

def search(value):
    try:
        sql  ='select * from vstudent where name like ? or id like ? or dname like ?'
        value = f'%{value}%'
        cur.execute(sql, (value, value, value,))
        rows = cur.fetchall()
        list=[]
        for row in rows:
            stu = Student()
            stu.id = row[0]
            stu.dept = row[1]
            stu.name = row[2]
            stu.dname = row[3]
            list.append(stu)
        return list
    except Exception as err:
        print('검색오류:', err)
    finally:
        pass

def newID():
    try:
        sql ='select max(id)+1 from student'
        cur.execute(sql)
        row = cur.fetchone()
        new_id = row[0]
        return new_id
    except Exception as err:
        print('코드생성:', err)
    finally:
        pass

def insert(stu):
    try:
        sql = 'insert into student(id, name, dept) values(?,?,?)'
        cur.execute(sql, (stu.id, stu.name, stu.dept,))
        con.commit()
    except Exception as err:
        print('입력오류:', err)
    finally:
        pass

def listDept():
    try:
        sql = 'select * from dept'
        cur.execute(sql)
        rows = cur.fetchall()
        list = []
        for row in rows:
            dept = Dept()
            dept.code = row[0]
            dept.dname = row[1]
            list.append(dept)
        return list
    except Exception as err:
        print('학과목록:', err)

def inputDept(title, type):
    depts = listDept()
    for dept in depts:
        print(f'{dept.code}.{dept.dname}', end='|')    
    print()
    codes = [dept.code for dept in depts]
    while True:
        code = input(title)
        if code=='' and type==5:
            return ''
        elif code=='' and type==1:
            print('학과코드는 반드시 입력하세요!')
        elif not code.isnumeric():
            print('학과코드는 숫자로 입력하세요!')
        elif codes.count(int(code))==0:
            print(f'{min(codes)}~{max(codes)} 코드번호를 입력하세요!')
        else:
            return int(code)  

def read(id):
    try:
        sql = 'select id,name,dept,dname from vstudent where id=?'
        cur.execute(sql, (id,))
        row = cur.fetchone()
        if row!=None:
            stu = Student()
            stu.id = id
            stu.name =row[1]
            stu.dept = row[2]
            stu.dname = row[3]
            return stu 
    except Exception as err:
        print('학번읽기오류:',err)

def delete(id):
    try:
        sql = 'delete from student where id=?'
        cur.execute(sql, (id,))
        con.commit()
    except Exception as err:
        print('학생삭제오류:', err)

def update(stu):
    try:
        sql = 'update student set name=?, dept=? where id=?'
        cur.execute(sql, (stu.name, stu.dept, stu.id,))
        con.commit()
    except Exception as err:
        print('학생수정오류:',err)

if __name__=='__main__':
    code = inputDept('학과코드>', 1)
    