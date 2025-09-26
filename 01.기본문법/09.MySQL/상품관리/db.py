import pymysql

con = pymysql.connect(
    host='192.168.0.28',
    user='web',
    password='pass',
    db = 'shop',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor,
    port=3306
)
cur = con.cursor()