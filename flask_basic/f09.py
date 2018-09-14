'''
단축키 : ctrl + shift + b -> 클릭 ->클릭 ->others ->task.json
등록 : ctrl + shift + b -> 클릭 ->tasks.json 이름 선택(그 전에 미리 설정해주고))) 
---------------------------------------------------------------
get 방식으로 전달된 데이터 가져오기 
'''
#1. 모듈 가져오기
from flask import Flask ,url_for,render_template,request#첫글자가 대문자이기 때문에 클래스일 확률이큼.
#2. 앱 정의
app = Flask(__name__)
#3. 라우트
#http://localhost:5000?bookid=123456789&no=s20
#get 방식으로 데이터 전달 방법
#url + ? + 키 = 값 + 키 = 값 + ....
#홈화면 한정 / 있어도되고 없어도 되고
@app.route('/')
def home():
    #get 방식으로 전달된 데이터 획득
    bookid=request.args.get('bookid')
    no    =request.args['no']#indexing 하지만, 불러 오지 못할 경우 error로 서버다운
    
    print(bookid,no)
    return render_template('f09.html',bid=bookid,number=no)
#4. 서버가동
if __name__=='__main__':
    app.run(debug=True)    

    print('본 모듈은 단독으로 구동시에만 정상 작동 합니다.')

