from flask import Blueprint

'''
웹 서비스나 미들웨어 어플리케이션 설계시 기능을 정리해서
계열을 나누면 => prefix 유추가됨 
ex) 회원 => member
메인서비스 => main
주식 => stock or trade~ ...
'''
# http://localhost:3000/main/~
blueprintMain = Blueprint('mainProc',
  __name__,
  template_folder='templates',
  static_folder='static'
)

# http://localhost:3000/login/~
blueprintLogin = Blueprint('loginProc',
  __name__,
  template_folder='templates',
  static_folder='static'
)
