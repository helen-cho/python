from flask import Blueprint
from dao import reply as DAO

bp = Blueprint('reply', __name__, url_prefix='/reply')

@bp.route("/list.json/<int:bid>")
def list(bid):
  rows = DAO.list(bid)
  return rows