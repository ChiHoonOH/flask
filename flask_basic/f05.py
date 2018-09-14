'''
URL 끝처리
ex) /pro /pro/
'''
#1. 모듈 가져오기
from flask import Flask #첫글자가 대문자이기 때문에 클래스일 확률이큼.
#2. 앱 정의
app = Flask(__name__)
#3. 라우트
@app.route('/')
#처리할 친구
def home():
    return 'hello world flask web'

@app.route('/pro')#내 가설- 여기 뒤에 뭔가를 붙여 줄 거 같다.
def pro():
    return "I'm pro"
#/pro2 => /pro2
#/pro2/ => /pro2/,/pro2
@app.route('/pro2/')
def pro2():
    return "I'm pro2"

#4. 서버가동
if __name__=='__main__':
    app.run(debug=True)    
else:
    print('본 모듈은 단독으로 구동시에만 정상 작동 합니다.')

