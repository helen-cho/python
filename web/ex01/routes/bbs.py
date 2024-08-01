from flask import Blueprint, render_template, request
from dao import bbs
import json

bp = Blueprint('bbs', __name__, url_prefix='/bbs')

@bp.route('/')
def list():
  return render_template(
    'index.html', title='게시판', pageName='bbs/list.html')

@bp.route('/list.json')
def listJSON():
  args = request.args
  page = args['page']
  size = args['size']
  print(page, size)
  list = bbs.list(page, size)
  total = bbs.total()
  data = {'total':total.get('cnt'), 'list':list}
  return data

@bp.route('/insert')
def insert():
  return render_template(
    'index.html',title='글쓰기', pageName='bbs/insert.html')

@bp.route('/insert', methods=['POST'])
def insertPost():
  req = json.loads(request.get_data())
  #print(req)
  result = bbs.insert(req)
  return result

@bp.route('/<int:bid>')
def read(bid):
  vo=bbs.read(bid)
  return render_template(
    'index.html', bbs=vo, title='게시글정보', pageName='bbs/read.html')

@bp.route('/<int:bid>', methods=['DELETE'])
def delete(bid):
  result = bbs.delete(bid)
  return result

@bp.route('update/<int:bid>')
def update(bid):
  vo=bbs.read(bid)
  return render_template(
    'index.html', bbs=vo, title='정보수정', pageName='bbs/update.html')

@bp.route('update', methods=['POST'])
def updatePost():
  req = json.loads(request.get_data())
  result = bbs.update(req)
  return result
