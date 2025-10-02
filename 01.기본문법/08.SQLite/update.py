import sqlite3
import os
path = os.path.dirname(os.path.realpath(__file__))
db_name = path + '/juso.db'

con = sqlite3.connect(db_name)
cursor = con.cursor()

sql = "update juso set name=?, address=? where seq=?"
seq = int(input('번호>'))
name = input('이름>')
address = input('주소>')

cursor.execute(sql, (name, address, seq,))
con.commit()

cursor.close()
con.close()