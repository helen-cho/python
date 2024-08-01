from dao import db

def list(bid):
  try:
    with db.connection.cursor() as cursor:
      sql="select *, date_format(regDate,'%%Y-%%m-%%d %%T') fmtDate \
          from reply\
          where bid=%s\
          order by rid desc"
      cursor.execute(sql, bid)
      rows = cursor.fetchall()
      return rows
  except Exception as err:
    print('목록오류', err)
  finally:
    cursor.close()