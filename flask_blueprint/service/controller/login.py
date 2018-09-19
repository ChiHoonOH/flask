from flask import render_template, request,url_for,session,jsonify,redirect,make_response
from service.app_blueprint import blueprintLogin as m
from service.model.member import Member
from service.app_database import dao
#회원가입(/login/signup),
@m.route('/signup',methods=['GET','POST'])
def signup():
      if request.method == 'GET':
            return render_template('signup.html')
      else:
            username=request.form['username']
            email=request.form['email']
            password=request.form['password']
            #잘 데이터가 들어왔다 치고 값 누락 체크 배제
            #회원가입 처리를 ORM으로 하기 위해
            #tbl_member 테이블과 연결된 Member를 가져온다.
            #row 하나를 생성했다.
            member = Member(username,email,password)
            #row 추가
            dao.add(member)
            #실제 반영
            dao.commit()

            return '''
            <script>
                  alert('가입성공');
                  document.location.href="{url}"
            </script>
            '''.format(url=url_for('loginProc.home'))

#수정(/login/update), 

def change(text):   
    return(text[:1]+'*'*len(text[1:-1])+text[-1:])

@m.route('/update',methods=['GET','POST'])
def update():
      member = dao.query(Member).filter_by(email=session['email']).first()#filter_by-where문
      if request.method == 'GET':
            #email를 기준으로 조회
            
            #화면에 비번 출력 => ***... 숨김
            
            #새로운 비번 입력창
            #수정 ->처리
            return render_template('update.html',pwd=change(member.password))
            #return render_template('update.html',password=member['password']
      else:
            password=request.form.get('password')
            member.password = password
            dao.commit()
            # /main으로 이동
            return redirect(url_for('mainProc.home'))

            
# 삭제(/login/delete), 
@m.route('/delete')
def delete():
      #회원정보 획득
      member=dao.query(Member).filter_by(email=session['email']).first()
      if member:
            #님아 로그아웃 아니고 탈퇴임
            dao.delete(member)
            print('해당맴버가 삭제 되었습니다.')
            dao.commit()
            return redirect(url_for('loginProc.logout'))
      else:  
            return '''
                   <script>
                        alert('삭제실패');
                        document.location.href="{0}"
                  </script>
                   '''.format(url_for('loginProc.home'))

      
      
# 로그인(/login),
@m.route('/',methods=['GET','POST'])
def home():      
      if request.method =='GET':
            #쿠키를 읽어서 로그인의 아이디에 설정한다. =>원래는 로그인 승인 받아야함.
            email = request.cookies.get('email')
            return render_template('login.html',email=email)
      else:#회원 조회(데이터는 잘왔다 전제)
            
            email=request.form['email']
            password=request.form['password']            
            member = dao.query(Member).filter_by(email=email,password=password).first()#filter_by-where문
            print(member)
            if member:
                  #session['user']=jsonify(member)#응 안됨 json 변환이 안됨
                  #방법1: 개별 정보 저장
                  session['username']=member.username
                  session['email']=email
                  print(session)
                  res_text ='''
                  <script>
                        alert('로그인성공');
                        document.location.href="{0}"
                  </script>
                   '''.format(url_for('loginProc.update'))
                  res=make_response(res_text)
                  res.set_cookie('email',email)
                  return res
            else:
                   return '''
                      <script>
                        alert('로그인실패');
                        history.back();
                        </script>                        
                  '''
            #dao.query(Member => 반환타입)
            #회원 정보 조회
            
# 로그아웃(/login/logout)
@m.route('/logout')
def logout():
      # while session:
      #       session.pop()
      print('pre-session:',session)
      for element in session:
            #세션제거
            session[element]=False
            #로그인으로 이동
      session.clear()
      print('로그아웃이 완료 되었습니다.')
      print('session:',session)
      return redirect(url_for('loginProc.home'))

# # ~/login
# @m.route('/')
# def home():
#   return '로그인 홈페이지'
# # ~/login/update
# @m.route('/update')
# def update():
#   print ( '/login/update call ' )
#   return 'update 홈페이지'
