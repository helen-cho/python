from flask import Blueprint, render_template
from dao import bbs

bp = Blueprint('bbs', __name__, url_prefix='/bbs')

@bp.route('/')
def list():
  return render_template(
    'index.html', title='게시판', pageName='bbs/list.html')

@bp.route('/list.json')
def listJSON():
  return bbs.list()