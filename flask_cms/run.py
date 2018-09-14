from flask import Flask,render_template,redirect,url_for,request,session#hash값을 key값으로가짐
from service.model import login_sql
app=Flask(__name__)
#세션키 설정 : 중복되지 않는 값
app.secret_key = 'xzcfxfsafsdrsfsda'


@app.route('/')
def home():
    #세션 체크
    if not 'user_id' in session:return render_template('login.html')
    
    return render_template('index.html',title='cms based flask')
@app.route('/login',methods=['GET','POST'])
def login():    
    if request.method == 'GET':      
        return render_template('login.html')  
    else:   
       #1.아이디 비번 획득 ->method? => post
        uid=request.form.get('uid') #form은 indexing이든 get이든 nullpoint에러 안뜸
        upw=request.form['upw']       
        if uid and upw:#정상                        
            row = login_sql(uid,upw)
            print('row:',row)
            if row:                
                session['user_id']=uid#session은 dictionary
                session['user_name']=row['name']                
                return redirect(url_for('home'))#url_for의 return 값은 아마 url
            else:
                return render_template('alert.html',msg='회원이 아닙니다.')
            #4. 회원이 맞으면 ok -> 세선생성(후처리) => 서비스 이동
            #5. 회원이 아니면 fail -> 경고 처리후 돌려 보낸다.
            
        else:            
            #2. 데이터가 없는 경우 ? => 경고 처리 하고돌려 보낸다.
            return render_template('alert.html',msg='입력이 정확하지 않습니다.') 

@app.route('/logout')
def logout():
    #세션제거
    if 'user_id' in session :session.pop('user_id')
    if 'user_name' in session :session.pop('user_name')
    
    
    #홈페이지이동
    return redirect(url_for('home'))
    
if __name__=='__main__':
    app.run(debug=True)