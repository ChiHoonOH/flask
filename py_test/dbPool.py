'''
파이썬에서 RDBMS를 접속 하는데
-class 형식으로 구성
-디비 커낵션 수백개 유지하여 = > 동접처리율 높임
-풀링 지원
pip install DBUtils
'''

import pymysql as my
from DBUtils.PooledDB import PooledDB
'''
a=1
b=1
del b =>참조 해제
'''
#tbl_uploadbbs에 대응하는 class(orm 아님) #java의 dto라고 생각하면된다.
class PostModel:
    '''
    맴버 변수
    '''
    id=None
    title=None
    contents=None
    author=None
    fileurl=None
    regdate=None
    '''
    생성자
    '''
    def __init__(self,title,contents,author,fileurl):
        self.title=title
        self.contents=contents
        self.author=author
        self.fileurl=fileurl

    '''
    객체정보
    '''

    def __repr__(self):
        return '''<PostModel
            title=%s, contents=%s, author=%s, fileurl=%s
        >'''.format(self.title,self.contents,self.author,self.fileurl)
#풀링 기반으로 커넥션을 관리하고 쿼리를 수행하는 방식
class DBHelper:
    '''
    맴버변수
    '''
    #풀링객체(디바와 연결된 커넥션을 가지고 있는 객체)-300개가 붙어도 상관 없다.
    connectionPool=None
    #최대 커넥션 수
    MAX_CONN = 100


    #생성자
    def __init__(self):
        self.initPool()
    #소멸자
    def __del__(self): #__del__함수는 참조해제
        self.freePool()
    #맴버함수(기능담당)
    def initPool(self):
        self.connectionPool = PooledDB(
            creator = my, #커넥션을 수행할 모듈명(pymysql)
            host='pythondb.c69gi2s1odpt.ap-northeast-2.rds.amazonaws.com',#서버주소
            user='root',
            password='12341234',
            database='pythondb',
            autocommit=False, #커밋 자동 처리 여부
            charset='utf8',  #문자열처리 인코딩
            cursorclass= my.cursors.DictCursor,#select 시 결과물을 dict 형태로 반환
            blocking=False,     #쿼리간 블럭(?)
            maxconnections=self.MAX_CONN
        )

    def freePool(self):
        #풀링을 닫으면 커넥션이 모두 해제된다.
        if self.connectionPool:
            self.connectionPool.close()

    #맴버함수(쿼리담당)
    def select_data(self):
        rows = None # 쿼리 결과
        conn = None        
        try:            
            #커넥션 빌려쓰기
            conn =self.connectionPool.connection()
            with conn.cursor() as cursor:
                sql    = 'select * from tbl_uploadbbs order by id desc limit 0, 10; '            
                cursor.execute( sql )
                rows   = cursor.fetchall()
        except Exception as e:
            rows = None
            print('에러->',e)
        # 커넥션 반납
        conn.close()
        # 결과 리턴
        return rows

#테스트 코드

if __name__=='__main__':
    helper=DBHelper()
    print(helper.select_data())
