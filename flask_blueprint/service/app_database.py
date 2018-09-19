'''
DB 매니저
ORM 방식 사용(object relation mapping) 
python에서 database 처리시 사용 모듈 : sqlalchemy
pip install sqlalchemy
sqlalchemy가 pymysql를 래핑해서 사용
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# 디비 연결 및 관리, 초기화 담당 
class DBManager:
  '''
  맴버 변수
  '''
  __engine  = None
  __session = None
  '''
  정적 함수 -> 객체를 생성하지 않고 클레스명.함수 사용
  @staticmethod를 사용하면 정적 함수가 되서 1번 인자에
  self를 사용하지 않는다 
  '''
  # 디비와 연결 처리 및 세션(연결된 정보) 처리
  @staticmethod
  def init(db_url, db_log_flag=True):
    # 1. 엔진 생성
    DBManager.__engine  = create_engine( db_url, echo=db_log_flag )
    # 2. 세션 생성
    DBManager.__session = scoped_session( sessionmaker(
      autocommit=False,
      autoflush=False,
      bind=DBManager.__engine
    ) )
    # 3. 세션을 여기 저기서 사용하기 위해 전역변수에 설정
    global dao
    dao = DBManager.__session
    
  @staticmethod
  def init_db():
    # 테이블이 없으면 생성 -> model에서 작성
    from service.model import member #모듈
    from service.model import Base #객체

    # 테이블이 없으면 모든 테이블 생성 -> Base를 상속 받으면 다 영향을 받음
    Base.metadata.create_all(bind=DBManager.__engine)

    pass
    

# 디비 세션
dao = None