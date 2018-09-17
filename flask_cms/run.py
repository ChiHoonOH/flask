from flask import Flask,render_template,redirect,url_for,request,session,jsonify#hash값을 key값으로가짐
from service.model import login_sql,select_tradeLastData as tradeList,select_searchTradeCode as searchName
import os
from service.model import insert_data,select_data
app=Flask(__name__)
#세션키 설정 : 중복되지 않는 값
app.secret_key = 'xzcfxfsafsdrsfsda'
#print('자징 디렉토리: %s/static/upload/' % os.getcwd())
@app.route('/')
def home():
    #세션 체크
    if not 'user_id' in session:
        return render_template('login.html')
    
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

#신규 페이지 이식 => 기능을 추가하는 방법(메뉴 추가)

@app.route('/search',methods=['GET','POST'])
def search():#미드웨어 서버  
     
    if request.method == 'GET':#검색화면
        rows=tradeList()
        return render_template('tradeSearch.html',trades=rows)
    else:#검색처리(ajax)
         #검색어 획득
        keyword = request.form.get('keyword')#post방식으로 받았기 때문에 form으로 변경
        #쿼리 수행
        rows    = searchName(keyword)
        #json 형식으로 변환(sequence type->변환 특히 그 키 있는 형식을 변환할때 좋다.)
        result = jsonify(rows) 
        
        return result

# 업로드 페이지 구현 
@app.route('/upload',methods=['GET','POST'])        
def upload():
    if request.method == 'GET':#html 화면 처리
        #index.html 카피해서 uploadForm.html준비
        #index_sub.html 카피해서 uploadForm_sub.html준비
        #render_template()처리
        return render_template('uploadForm.html')
    else:#업로드된 파일 저장-> 디비에 기록 -> 성공여부 처리 -> 돌아간다.(리스트 or 입력)
        #요청데이터 획득
        #-제목
        title=request.form.get('title')
        #-내용
        contents=request.form.get('contents')
        #-파일
        fileData = request.files.get('fileData')
        print(title,contents,fileData)        
        ##-파일의 물리적 저장
        #경로 획득
        checkPath='%s\\flask_cms\\static\\upload\\%s'%(os.getcwd(),session['user_id'])
        path=checkPath+'\\'+fileData.filename
        if not os.path.exists(checkPath):
            os.mkdir(checkPath)    
        fileData.save(path)
        #path=os.getcwd()+'\\flask_cms\\static\\upload\\'+session.get('user_id')+fileData.filename

        #성공하면 upload/uid/파일 방식으로 저장시도.
        #디비에 입력(제목,내용,파일의 url 경로)
        downUrl='/static/upload/%s/%s'%(session['user_id'],fileData.filename)
        if insert_data(title,contents,session['user_id'],downUrl):
            return render_template('alert.html',msg='업로드 성공',target_url='/scrapList')
        else:
            return render_template('alert.html',msg='업로드 실패')

@app.route('/scrapList')
def scrapList():
    return render_template('scrapList.html',scrap=select_data())

        
if __name__=='__main__':
    app.run(debug=True)