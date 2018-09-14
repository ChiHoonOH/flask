'''
파이썬 웹의 기본 골격
'''
#1. 모듈 가져오기
from flask import Flask #첫글자가 대문자이기 때문에 클래스일 확률이큼.
#2. 앱 정의
app = Flask(__name__)
#3. 라우트
#사용자가 요청을 분석해서 어떤 함수가 반응하여 응답할지를 정하는 과정
#요청 => request => ::브라우저 열고, 
#       주소창에 http://localhost:5000/login
#응답 => 요청을 분석해서 누가 처리 할 건지 던지고 => 처리할 함수가 요청 통해 전달된 데이터
#       를 획득하여 => html 생성 =>전달
#브라우저는 응답을 받아서 parsing을 수행하여 화면에 내용을 보이게 한다.
@app.route('/')
#처리할 친구
def home():
    return 'hello world flask web'
#4. 서버가동
if __name__=='__main__':
    app.run()    
else:
    print('본 모듈은 단독으로 구동시에만 정상 작동 합니다.')