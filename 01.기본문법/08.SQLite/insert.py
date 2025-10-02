import sqlite3
import os
path = os.path.dirname(os.path.realpath(__file__))
db_name = path + '/juso.db'

con = sqlite3.connect(db_name)
cursor = con.cursor()

sql="insert into juso(name, address) values('강감찬','부산시 동래구')"
cursor.execute(sql)
sql="insert into juso(name, address) values('홍길동','경기도 광명시')"
cursor.execute(sql)
sql="insert into juso(name, address) values('이순신','서울 강남구')"
cursor.execute(sql)

id = cursor.lastrowid

con.commit()
cursor.close()
con.close()

print(f'id:{id}')