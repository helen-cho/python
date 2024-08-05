from flask import Blueprint
from dao import bbs as bbsDAO

bp = Blueprint('bbs', __name__, url_prefix='/bbs')

@bp.route('/')
def list():
  rows = bbsDAO.list()
  return rows;