from flask import Flask, session, request, redirect, url_for

# Flask 객체 생성 #############
def create_flaskApp(configPath='resource/config.cfg'):
  app = Flask(__name__)
  # 세션키
  app.secret_key = 'jdhflwekaehfkwenflcj'
  # 환경변수 로드########################################################
  # 파일에서 로드 
  app.config.from_pyfile(configPath, silent=True) 
  # 객체에서 로드 
  from service.app_config import FalskWebConfig
  app.config.from_object(FalskWebConfig)
  printConfigLog( app.config.items() )
  ####################################################################
  # 데이터베이스 연결 처리
  from service.app_database import DBManager
  db_url = "mysql+pymysql://%s:%s@%s:%s/%s?charset=%s" % (
           app.config['DB_USER'],
           app.config['DB_PWD'],
           app.config['DB_URL'],
           app.config['DB_PORT'],
           app.config['DB_DATABASE'],
           app.config['DB_CHARSET']
  )
  # mysql+pymysql://root:12341234@localhost/pythondb?charset=utf8
  # mysql+pymysql://root:12341234@localhost:3306/pythondb?charset=utf8
  print( db_url )
  # 디비 연결 초기화
  # 원래 타입으로 가야하는데 문자열로 처리가 된 상황
  DBManager.init( db_url, eval(app.config['DB_LOG_FLAG']) )
  # 디비 초기화(테이블 생성등...)
  DBManager.init_db()
  #################################################################
  # 뷰처리(블루프린트-> url별로 기능 계열화해서 분업처리)
  from service.controller import main, login, user
  from service.app_blueprint import blueprintMain, blueprintLogin
  from service.controller import bp_user
  # 블루 프린트 등록 -> 해당 블루프린트도 라우트 권한이 생김
  app.register_blueprint(blueprintMain, url_prefix='/main')
  app.register_blueprint(bp_user, url_prefix='/user')
  app.register_blueprint(blueprintLogin, url_prefix='/login')
  ###############################################################
  # 요청과 응답에대한 감지 (전후 처리), 세션 처리
  initRoute( app )
  ############################################################### 
  # 에러등록처리
  # Flask 객체 리턴
  return app

# 요청과 응답에대한 감지 (전후 처리), 세션 처리
def initRoute(app):
  @app.before_first_request
  def before_first_request():#최초한번 요청 들어왔을때
    print('서버가 가동하고 최초 요청시 반응, 오직 한번만')
  
  @app.before_request#모든 요청이 지나가는곳
  def before_request():
    # 전처리: 세션체크
    #print( request.url.find('/login') )
    # index는 대상이 없으면 오류 발생
    #print( request.url )
    # /login 통과~>
    # 세션 없으면 컷->/login
    # if not 'email' in session:
    #   # 세션이 없는데 주소가 login이 아니다 -> /login  
    #   if request.url[-6:] == '/login' or request.url[-7:] == '/login/':
    #     #print( '로그인 패스' )
    #     pass
    #   else:
    #     #print( '세션 없으니 포워딩', url_for('loginProc.home') )
    #     # url_for( '블루프린트이름.함수명=>매칭url대체' )
    #     return redirect( url_for('loginProc.home') )
    print('요청할때마다 여기를 거친다 => 전처리 => 세션처리')
  
  @app.after_request
  def after_request( res ):
    print('매 요청이 처리되고 나서 실행된다. => 응답이 지나가는 곳')      
    return res
  
  @app.teardown_request
  def teardown_request( exception ):
    print('브라우저가 응답하고 나서 실행', exception)
    return ''
  
  @app.teardown_appcontext
  def teardown_appcontext( exception ):
    print('http 요청한 어플리케이션 컨텍스트가 종료되고 실행')


# 환경 변수 확인
def printConfigLog( config ):
  print( '\n'*5 )
  print( '-'*100 )
  #print( config )
  for key, value in config:
    print( key, value )
  print( '-'*100 )
  print( '\n'*5 )  


