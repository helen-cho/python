from flask import Blueprint, render_template

bp = Blueprint('scrap', __name__, url_prefix='/scrap')

@bp.route('/movie')
def movie():
  return render_template('index.html', title='무비챠트', pageName='scrap/movie.html')