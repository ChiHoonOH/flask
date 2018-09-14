'''
flask의 시그네처 포트 : 5000 #http는 80 임
debug 모드 설정
'''
#1. 모듈 가져오기
from flask import Flask #첫글자가 대문자이기 때문에 클래스일 확률이큼.
#2. 앱 정의
app = Flask(__name__)
#3. 라우트
@app.route('/')
#처리할 친구
def home():
    return 'hello world3'
#4. 서버가동
if __name__=='__main__':
    #디버깅모드에서 py 수정하면 바로 서버가 리로드 된다. 굳이 죽였다가 살릴필요 없
    #app.run(debug=True)    
    app.debug =True#app 객체의 값의 내용을 변경해준다.
    app.run()
else:
    print('본 모듈은 단독으로 구동시에만 정상 작동 합니다.')

