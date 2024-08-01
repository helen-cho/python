from flask import Blueprint, request
from dao import reply as DAO
import json

bp = Blueprint('reply', __name__, url_prefix='/reply')

@bp.route("/list.json/<int:bid>")
def list(bid):
  rows = DAO.list(bid)
  if rows:
    return rows
  else:
    return []
  
@bp.route('/insert', methods=['POST'])
def insert():
  req = json.loads(request.get_data())
  result = DAO.insert(req)
  return result