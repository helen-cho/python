from flask import Blueprint, render_template, request, redirect
import json
from dao import users

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/login')
def login():
  return render_template(
    'index.html', title='로그인', pageName='users/login.html')

@bp.route('/login', methods=['POST'])
def loginPost():
  req = json.loads(request.get_data())
  uid=req['uid']
  upass=req.get('upass')
  row = users.read(uid)
  result=0
  if row:
    if row.get('upass')==upass:
      result=1
    else:
      result=2
  return str(result)

@bp.route('/insert', methods=['POST'])
def insertPost():
  files=request.files.getlist('file')
  for file in files:
    file.save('static/images/' + file.filename)
  form=request.form
  print(form.get("uid"), form.get('uname'))
  return redirect('/')
  

@bp.route('/insert')
def insert():
  return render_template('index.html', title='사용자등록', pageName='users/insert.html')