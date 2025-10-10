import sqlite3
import os
path = os.path.dirname(os.path.realpath(__file__))
db_name = path + '/juso.db'

con = sqlite3.connect(db_name)
cursor = con.cursor()

sql = "select * from juso"
cursor.execute(sql)

rows = cursor.fetchall()
for row in rows:
    print(f'번호:{row[0]}, 이름:{row[1]}, 주소:{row[2]}')

cursor.close()
con.close()