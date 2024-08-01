from flask import Blueprint, request
from dao import reply as DAO
import json

bp = Blueprint('reply', __name__, url_prefix='/reply')

@bp.route("/list.json/<int:bid>")
def list(bid):
  args = request.args
  row = DAO.total(bid)
  rows = DAO.list(bid, args)
  data = {'total':row.get('cnt'), 'list':rows}
  return data
  
@bp.route('/insert', methods=['POST'])
def insert():
  req = json.loads(request.get_data())
  result = DAO.insert(req)
  return result

@bp.route('/<int:rid>', methods=['DELETE'])
def delete(rid):
  result = DAO.delete(rid)
  return result

@bp.route('/update', methods=['POST'])
def update():
  req = json.loads(request.get_data())
  result = DAO.update(req)
  return result