from flask import Blueprint, request
from dao import bbs as bbsDAO
import json

bp = Blueprint('bbs', __name__, url_prefix='/bbs')

@bp.route('/')
def list():
  args = request.args
  rows = bbsDAO.list(args)
  row = bbsDAO.total()
  #print(rows)
  return {'total':row.get('cnt'), 'list':rows}

@bp.route('/', methods=['POST'])
def insert():
  data = json.loads(request.get_data())
  result = bbsDAO.insert(data)
  return result

@bp.route('/<int:bid>', methods=['DELETE'])
def delete(bid):
  result = bbsDAO.delete(bid)
  return result

@bp.route('/<int:bid>')
def read(bid):
  result = bbsDAO.read(bid)
  return result

@bp.route('/', methods=['PUT'])
def update():
  data = json.loads(request.get_data())
  result = bbsDAO.update(data)
  return result