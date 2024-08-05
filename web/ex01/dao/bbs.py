from dao import db

def list(page, size):
  page = int(page)
  size = int(size)
  start=(page-1) * size
  try:
    with db.connection.cursor() as cursor:
      sql = "select *, date_format('%%Y-%%m-%%d %%T', regDate) fmtDate \
            from bbs order by bid desc \
            limit %s, %s"
      cursor.execute(sql, (start, size))
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
      db.connection.commit()
      return 'success'
  except Exception as err:
    print('등록오류:', err)
    return 'fail'
  finally:
    cursor.close()

def read(bid):
  try:
    with db.connection.cursor() as cursor:
      sql="select *, date_format(regDate,'%%Y-%%m-%%d %%T') fmtDate \
          from bbs where bid=%s"
      cursor.execute(sql, bid)
      row = cursor.fetchone()
      return row
  except Exception as err:
    print('읽기오류:', err)
  finally:
    cursor.close()

def delete(bid):
  try:
    with db.connection.cursor() as cursor:
      sql= "delete from bbs where bid=%s"
      cursor.execute(sql, bid)
      db.connection.commit()
      return 'success'
  except Exception as err:
    print('삭제오류:', err)
    return 'fail'
  finally:
    cursor.close()    

def update(bbs):
  try:
    with db.connection.cursor() as cursor:
      sql= "update bbs set title=%s, contents=%s, regDate=now() \
            where bid=%s"
      cursor.execute(sql, (bbs.get('title'), bbs.get('contents'), bbs.get('bid')))
      db.connection.commit()
      return 'success'
  except Exception as err:
    print('수정오류:', err)
    return 'fail'
  finally:
    cursor.close()

def total():
  try:
    with db.connection.cursor() as cursor:
      sql="select count(*) cnt from bbs"
      cursor.execute(sql)
      row = cursor.fetchone()
      return row
  except Exception as err:
    print('게시글수오류:', err)
  finally:
    cursor.close()   

