import sqlite3
import os
path = os.path.dirname(os.path.realpath(__file__))
db_name = path + '/juso.db'

con = sqlite3.connect(db_name)
cursor = con.cursor()

sql = 'drop table if exists juso'
cursor.execute(sql)
con.commit()

sql  = 'create table juso('
sql += 'seq integer primary key autoincrement,'
sql += 'name char(20),'
sql += 'address char(200))'
cursor.execute(sql)
con.commit()

cursor.close()
con.close()