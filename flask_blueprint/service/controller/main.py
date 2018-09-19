'''
메인 서비스 관련 사항만 모여있다
url path : ~/main/~
@app.route()
app이라는 부분은 블루프린트 객체로 받아서 사용 
'''
from flask import render_template, request,session,url_for
from service.app_blueprint import blueprintMain as app

# http://localhost:3000/main
@app.route('/')
def home():
  return '''
  <p>main 홈페이지:<b>{0}</b>님 10번째 방문</p>
  <a href='{1}'>회원탈퇴</a>

  '''.format(session['username'],url_for('loginProc.delete'))