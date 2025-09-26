class Student:
    def __init__(self): #객체를 만드는 생성자
        self.no = ''
        self.name = ''
        self.dept = '컴정과'
        self.birthday = '00-10-04'
    
    def info_print(self): #학생 속성을 출력한 메서드(함수)
        print(f"학번:{self.no}", end=",")
        print(f"성명:{self.name}", end=",")
        print(f"학과:{self.dept}", end=",")
        print(f"생일:{self.birthday}")

    def info(self): #학생 정보 생성하는 메서드(함수)
        return {'no':self.no, 'name':self.name, 'dept':self.dept, 'birthday':self.birthday}

    
if __name__=='__main__':
    s = Student()
    s.no='01'
    s.name='홍길동'
    s.birthday='02-12-17'
    print(s.info_print())
