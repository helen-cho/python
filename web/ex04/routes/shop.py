from flask import Blueprint, render_template, request

bp = Blueprint('shop', __name__, url_prefix='/shop')

@bp.route('/search')
def search():
  return render_template(
    'index.html', title='상품검색', pageName='shop/search.html')