'''
- url 사용시(서버프로그램 내부에서) 하드코딩하지 않는다.
- 만약 url이 변경되면 사용한 모든 곳을 다 고쳐야 된다.(유지보수)
- url_for() => 라우트는 함수와 연결되어 있다.=>함수명 ->url을 찾는다.  
'''
#1. 모듈 가져오기
from flask import Flask,url_for #첫글자가 대문자이기 때문에 클래스일 확률이큼.

#2. 앱 정의
app = Flask(__name__)
#3. 라우트
@app.route('/ppp')
def home():
    return 'hello world flask web'

@app.route('/login')
def login():
    return 'login page'

@app.route('/user/<uid>')
def userCheck(uid):pass
#url테스트
# i/o 계열에서 열고 업무보고 닫기를 하는데 닫기를 누락 방지
with app.test_request_context(): #이거 뭥미?
    print('홈페이지주소-',url_for('home'))#home 함수이름
    print('로그인주소-',url_for('login'))
    print('동적파라미터 주소-',url_for('userCheck',uid='bu'))
#url이 바뀌어도 함수는동작함.

#4. 서버가동
if __name__=='__main__':
    app.run(debug=True)    
else:
    print('본 모듈은 단독으로 구동시에만 정상 작동 합니다.')

