from dao import db

def list():
  try:
    with db.connection.cursor() as cursor:
      sql="select * from bbs\
           order by bid desc\
           limit 0, 5"
      cursor.execute(sql)
      return cursor.fetchall()
  except Exception as err:
    print('목록오류:', err)
  finally:
    pass