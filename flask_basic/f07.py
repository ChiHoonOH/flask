'''
데이터 전달 방식 get,post
-GET: http 프로토콜의 header를 통해 전달 => 보안에 취약, 소량전달
-POST: http 프로토콜의 body를 통해 전달 => 보안에 뛰어남, 대량전달
'''
#1. 모듈 가져오기
from flask import Flask,request #첫글자가 대문자이기 때문에 클래스일 확률이큼.
#2. 앱 정의
app = Flask(__name__)
#3. 라우트
@app.route('/')
def home():
    return 'hello world flask web'
#로그인
@app.route('/login')#get 방식
def login():
    return 'login'
#url 하나가 get과 post를 모두 지원 하고 싶다.
@app.route('/login2',methods=['get','post'])
def login2():
    #~/login2 요청(get)=>로그인 폼
    #~/login2 요청(post)=>로그인 처리
    #==> restful이라고 한다.
    if request.method == 'GET':
        return 'login form'        
    else:
        return 'login process'
#4. 서버가동
if __name__=='__main__':
    app.run(debug=True)    
else:
    print('본 모듈은 단독으로 구동시에만 정상 작동 합니다.')

