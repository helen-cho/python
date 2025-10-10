import sqlite3
import os
path = os.path.dirname(os.path.realpath(__file__))
db_name = path + '/juso.db'

con = sqlite3.connect(db_name)
cursor = con.cursor()

sql = "delete from juso where seq=?"
seq = int(input("삭제번호>"))
cursor.execute(sql, (seq,))
con.commit()

cursor.close()
con.close()