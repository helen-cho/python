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
