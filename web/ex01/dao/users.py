from dao import db

def read(uid):
  try:
    with db.connection.cursor() as cursor:
      sql="select * from users where uid=%s"
      cursor.execute(sql, uid)
      row = cursor.fetchone()
      return row
  except Exception as err:
    print('읽기오류:', err)
  finally:
    pass