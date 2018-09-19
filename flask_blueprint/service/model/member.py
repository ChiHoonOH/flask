'''
맴버 테이블 대응
'''
from service.model import Base
from sqlalchemy import Column,Integer,String
# Base를 상속 받아야 ORM 사용 가능#응 그래서 ORM이 뭔데?
class Member(Base):
  # 테이블명
  __tablename__ = 'tbl_member'
  # 컬럼
  id        =Column(Integer,primary_key=True)
  username  =Column(String(50),unique=False)
  email     =Column(String(50),unique=True)
  password  =Column(String(50),unique=False)
  # 생성자
  def __init__(self,username,email,password):
    self.username = username
    self.email = email
    self.password = password
  
  # 객체값출력
  def __repr__(self):
    return '<Member username=%s email=%s password=%s>'% (self.username,self.email,self.password)
    
