'''
render_template : html 랜더링을 담당(동적으로 html을 구성)

'''
#1. 모듈 가져오기
from flask import Flask,request,render_template #첫글자가 대문자이기 때문에 클래스일 확률이큼.
#2. 앱 정의
app = Flask(__name__)
#3. 라우트
@app.route('/')
def home():
    return 'hello world flask web'
#로그인
@app.route('/login',methods=['get','post'])
def login():
    #~/login2 요청(get)=>로그인 폼
    #~/login2 요청(post)=>로그인 처리
    #==> restful이라고 한다.
    if request.method == 'GET':
        return render_template('login.html')#template에 넣으면 됨.
    else:
        return 'login process'
#4. 서버가동
if __name__=='__main__':
    app.run(debug=True)    
else:
    print('본 모듈은 단독으로 구동시에만 정상 작동 합니다.')

