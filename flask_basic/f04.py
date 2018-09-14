'''
동적 파라미터!!(서버로 전달하는 데이터)!!!
=>url(주소)에 데이터를 전달한다. 
=>쉽게 서버로 데이터를 전달 할 수 있다.
=>보안에 취약하다.
'''
#1. 모듈 가져오기
from flask import Flask #첫글자가 대문자이기 때문에 클래스일 확률이큼.
#2. 앱 정의
app = Flask(__name__)

#3. 라우트
@app.route('/')
#처리할 친구
def home():
    return 'hello world flask web'#화면에 찍어줌

#~/news/20180910130000
#~/news/adsadsad
#타입을 부여하지 않으면 문자열로 판단
#이렇게 news_id로 올 수 있는 타입 : int, float,path(경로)

@app.route('/news/<news_id>')
def news(news_id):#그냥 url 이름 갖다 쓰자.//함수의 인자로 넣어준다.
    return 'dynamic url {} response'.format(news_id)
    #return 'dynamic url %s response' % news_id

#정수 타입 동적 파라미터
#동적 파라미터를 두어서 별도로 체크 안해도 됨.
@app.route('/news2/<int:news_id>')#int 이외의 값을 입력하면 404에러 뜸
def news2(news_id):#그냥 url 이름 갖다 쓰자.//함수의 인자로 넣어준다.
    return 'dynamic url %s response' % news_id
    #%s는 모든 타입을 받아준다.

#path 타입 확인
#뒤에 /를 기준으로 무한대로 파라미터를 전달 할 수 있다.
#http://127.0.0.1:5000/news3/a@a.com/1234
#이메일(a@a.com)과 비번(1234)를 추출하여서
#당신의 이메일 a@a.com 비번 = 1234 입니다.
@app.route('/news3/<path:n>')
def news3(n):    
    print(n) 
    list_tmp = n.split('/')
    print(list_tmp)
    return '당신의 이메일 {} 비번은 {} 입니다.'.format(list_tmp[0],list_tmp[1])
#4. 서버가동
if __name__=='__main__':
    app.run(debug=True)    
else:
    print('본 모듈은 단독으로 구동시에만 정상 작동 합니다.')

