'''
단축키 : ctrl + shift + b -> 클릭 ->클릭 ->others ->task.json
등록 : ctrl + shift + b -> 클릭 ->tasks.json 이름 선택(그 전에 미리 설정해주고))) 
---------------------------------------------------------------
get 방식으로 전달된 데이터 가져오기 
'''
#1. 모듈 가져오기
from flask import Flask,url_for,render_template,request,redirect#첫글자가 대문자이기 때문에 클래스일 확률이큼.
from db.d08 import login_sql
#2. 앱 정의
app = Flask(__name__)
#3. 라우트
#http://localhost:5000?bookid=123456789&no=s20
#get 방식으로 데이터 전달 방법
#url + ? + 키 = 값 + 키 = 값 + ....
#홈화면 한정 / 있어도되고 없어도 되고
@app.route('/')
#처리할 친구
def home():
    return 'Home:hello world3'
@app.route('/login',methods=['GET','POST'])
def login():
    #get 방식으로 전달된 데이터 획득
    if request.method == 'GET':
        # uid=request.args.get('uid') 
        # password=request.args.get('pass')#indexing
        # date=request.args.get('date')
        return render_template('f10.html')  
    else:   
       #1.아이디 비번 획득 ->method? => post
        uid=request.form.get('uid') #form은 indexing이든 get이든 nullpoint에러 안뜸
        upw=request.form['upw']
       
        if uid and upw:#정상            
            #3. 데이터가 정상이면 디비 조회
            row = login_sql(uid,upw)
            print('row:',row)
            if row:
                #요청을 다른 url로 돌려준다.
                return redirect(url_for('home'))#url_for의 return 값은 아마 url
            else:
                return render_template('err.html',msg='회원이 아닙니다.')
            #4. 회원이 맞으면 ok -> 세선생성(후처리) => 서비스 이동
            #5. 회원이 아니면 fail -> 경고 처리후 돌려 보낸다.
            
        else:            
            #2. 데이터가 없는 경우 ? => 경고 처리 하고돌려 보낸다.
            return render_template('err.html',msg='입력이 정확하지 않습니다.')    
#4. 서버가동
if __name__=='__main__':
    app.run(debug=True) 
    print('본 모듈은 단독으로 구동시에만 정상 작동 합니다.')

