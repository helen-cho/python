from dao import db

def list():
  try:
    with db.connection.cursor() as cursor:
      sql = "select *, date_format(regDate,'%Y-%m-%d %T') fmtDate from bbs order by bid desc"
      cursor.execute(sql)
      rows = cursor.fetchall()
      return rows
  except Exception as err:
    print('목록오류:', err)
  finally:
    cursor.close()

def insert(bbs):
  try:
    with db.connection.cursor() as cursor:
      sql= "insert into bbs(title, contents, writer) \
            values(%s,%s,%s)"
      cursor.execute(sql, (bbs.get('title'), bbs.get('contents'), bbs.get('uid')))
      return 'success'
  except Exception as err:
    print('등록오류:', err)
    return 'fail'
  finally:
    cursor.close()
