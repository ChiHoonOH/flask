'''
파이썬 웹의 기본 골격
'''
#1. 모듈 가져오기
from flask import Flask ,url_for,render_template,request#첫글자가 대문자이기 때문에 클래스일 확률이큼.
#2. 앱 정의
app = Flask(__name__)
#3. 라우트
@app.route('/')
def home():
    return 'home.html'
#4. 서버가동
if __name__=='__main__':
    app.run(debug=True)    
else:
    print('본 모듈은 단독으로 구동시에만 정상 작동 합니다.')

