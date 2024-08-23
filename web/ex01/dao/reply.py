from dao import db

def list(bid, args):
  page = int(args['page'])
  size = int(args['size'])
  start = (page-1) * size 
  try:
    with db.connection.cursor() as cursor:
      sql="select *, date_format(regDate,'%%Y-%%m-%%d %%T') fmtDate \
          from reply\
          where bid=%s\
          order by rid desc\
          limit %s, %s"
      cursor.execute(sql, (bid, start, size))
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

def total(bid):
  try:
    with db.connection.cursor() as cursor:
      sql="select count(*) cnt from reply where bid=%s"
      cursor.execute(sql, bid)
      row = cursor.fetchone()
      return row
  except Exception as err:
    print('댓글수오류', err)
  finally:
    cursor.close()

def delete(rid):
    try:
      with db.connection.cursor() as cursor:
        sql="delete from reply where rid=%s"
        cursor.execute(sql, rid)
        db.connection.commit()
        return 'success'
    except Exception as err:
      print('삭제오류', err)
      return 'fail'
    finally:
      cursor.close()

def update(reply):
  try:
    with db.connection.cursor() as cursor:
      sql="update reply set contents=%s, regDate=now() where rid=%s"
      cursor.execute(sql, (reply.get('contents'), reply.get('rid')))
      db.connection.commit()
      return 'success'
  except Exception as err:
    print('수정오류', err)
    return 'fail'
  finally:
    cursor.close()