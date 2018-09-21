from flask import Flask, url_for, render_template, request, redirect, session, jsonify
# 리눅스상 프로그램 구동 구조가 달라서 수정
from flask_cms.service.model import loginSql, select_tradeLastData as tradeList, select_searchTradeCode as searchName
from flask_cms.service.model import insert_data, select_data

app = Flask(__name__)
# 세션키 설정 : 중복되지 않는 값
app.secret_key = 'zxkvnlasdvknkdjavmcascdds'

#import os
#print( '저장디렉토리 : %s\\static\\upload\\ ' % os.getcwd() )

@app.route('/')
def home():
  # 세션 체크
  print('세션 체크')
  if not 'user_id' in session: # 세션 객체 안에 user_id가 없으면
    return redirect( url_for('login') )
  return render_template('index.html', title='cms based flask')

@app.route('/logout')
def logout():
  # 세션 제거
  if 'user_id' in session:session.pop('user_id')
  if 'user_name' in session:session.pop('user_name')
  # 홈페이지 이동
  return redirect( url_for('home') )

@app.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'GET':
    return render_template('login.html')
  else:
    uid = request.form.get('uid')
    upw = request.form.get('upw')
    print(uid)
    if uid and upw: # 정상      
      row = loginSql(uid, upw)
      if row:      
        # 4. 회원이 맞으면 ok -> 세션생성(후처리) -> 서비스 이동
        # 세션 생성
        print('세션 생성 시작')
        session['user_id']   = uid
        session['user_name'] = row['name']
        print('세션 생성 완료')
        # 요청을 다른 url로 돌려준다        
        return redirect( url_for('home') )
      else:
        # 4. 회원이 아니면 fail-> 경고 처리후 돌려보낸다
        return render_template('alert.html', msg='회원이 아닙니다.')
    else:#비정상처리
      # 2. 데이터가 없는 경우?=> 경고 처리 돌려보낸다
      return render_template('alert.html', msg='입력이 정확하지 않습니다.')

# 신규 페이지 이식 => 기능을 추가하는 방법(메뉴 추가)
@app.route('/search', methods=['GET','POST'])
def search():
  if request.method == 'GET': # 검색 화면
    rows = tradeList()
    return render_template('tradeSearch.html', trades=rows)
  else: # 검색 처리 (ajax 대응)
    keyword = request.form.get('keyword') # post 방식 변경
    rows    = searchName(keyword)         # import 완료
    return jsonify(rows) 

# 업로드 페이지 구현
@app.route('/upload', methods=['GET','POST'])
def upload():
  if request.method == 'GET': # html 화면 처리
    # index.html 카피해서 uplaodForm.html 준비
    # index_sub.html 카피해서 uplaodForm_sub.html 준비
    # uplaodForm.html 내부에 uplaodForm_sub.html include 수정
    # render_template() 처리
    return render_template('uplaodForm.html')
  else: # 업로드된 파일 저장->디비에 기록->성공여부 처리->돌아간다(리스트 or 입력)
    # 요청 데이터 획득
    # 제목
    title    = request.form.get('title')
    # 내용
    contents = request.form.get('contents')
    # 파일
    fileData = request.files['fileData']
    print( title, contents, fileData.filename )
    # 경로 획득
    import os
    ############################################################
    # 1. 기본저장
    #fileData.save( '%s\\static\\upload\\%s' 
    #               % (os.getcwd(), fileData.filename) )
    # 파일을 물리적으로 저장
    ############################################################

    ############################################################
    # 2. 사용자 uid 밑으로 저장
    # 2-1. 사용자 uid 폴더가 존재하는가?
    checkPath = '%s\\static\\upload\\%s' % (os.getcwd(), session['user_id'])
    if not os.path.exists( checkPath ):
      # 폴더( ~/upload/사용자아이디 ) 생성
      os.mkdir( checkPath )
    ############################################################
    # 2-2. 파일 저장
    path = '%s\\static\\upload\\%s\\%s' % (os.getcwd(), session['user_id'], fileData.filename)
    fileData.save( path )
    ############################################################
    # 파일의 url 경로를  return값으로 출력
    downUrl = '/static/upload/%s/%s' % (session['user_id'], fileData.filename)
    # 디비에 입력 (제목, 내용, 파일의 url 경로)
    if insert_data( title, contents, session['user_id'], downUrl ):    
      return render_template('alert.html', msg='업로드성공', target_url='/scrapList')
    else:
      return render_template('alert.html', msg='업로드실패')

# 자료실 게시판 리스트 
@app.route('/scrapList')
def scrapList():
  return render_template('scrapList.html', scarp=select_data() )

if __name__ == '__main__':
  app.run(debug=True)