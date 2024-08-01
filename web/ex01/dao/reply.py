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

def insert(reply):
    try:
      with db.connection.cursor() as cursor:
        sql="insert into reply(bid, contents, writer)\
            values(%s, %s, %s)"
        cursor.execute(sql, 
          (reply.get('bid'), reply.get('contents'), reply.get('uid')))
        db.connection.commit()
        return 'success'
    except Exception as err:
      print('등록오류', err)
      return 'fail'
    finally:
      cursor.close()
