# 모둘 가져오기 : RDBMS 제품 mysql 계열을 쿼리하는 모듈
import pymysql as my

class DBMgr:
    '''
    맴버 변수
    '''
    conn = None
    '''
    생성자 
    '''
    def __init__(self):
        # 맴버 변수 초기화
        self.initDB()
    '''
    맴버 함수
    '''
    # 디비 접속
    def initDB(self):
        # 커넥션이 1개이다 => 동접이 많아지면 응답이 느려질것이다 => 풀링, ORM, ..
        try:
            self.conn = my.connect(
                            host='127.0.0.1', #'localhost',                    
                            user='root',
                            password='12341234',
                            db='pythondb',
                            charset='utf8',
                            cursorclass=my.cursors.DictCursor
                            )
        except Exception as e:
            print( '디비 커넥션 오류 ', e )
            self.conn = None

    # 디비 해제
    def freeDB(self):
        if self.conn:
            self.conn.close()

    # 자료실 데이터 가져오기(페이징X)    
    def select_data(self):
        rows = None # 쿼리 결과        
        try:            
            with self.conn.cursor() as cursor:
                sql    = 'select * from tbl_uplaodBbs order by id desc limit 0, 10; '            
                cursor.execute( sql )
                rows   = cursor.fetchall()
        except Exception as e:
            rows = None
            #print('에러->',e)
        # 결과 리턴
        return rows

    # 자료실 업로드 처리
    def insert_data( self, title, contents, uid, fileUrl ):
        result = 0
        # ===========================================        
        try:            
            with self.conn.cursor() as cursor:
                sql    = '''
                        insert into tbl_uplaodBbs(title, contents, author, fileUrl, regdate) 
                        values ( %s, %s, %s, %s, now() );
                        '''
                cursor.execute( sql, (title, contents, uid, fileUrl))
            self.conn.commit()        
            result = self.conn.affected_rows()
        except Exception as e:
            result = 0
            #print('에러->',e)
        # ===========================================
        return result

    # flask_basic>db>d08.py에서 카피
    def loginSql(self, uid, upw):
        row  = None # 쿼리 결과        
        try:            
            # 3. 쿼리수행 ==========================================
            # 3-1. 커서 획득
            with self.conn.cursor() as cursor:
                # 3-2. sql 준비
                sql    = '''
                            select 
                                * 
                            from 
                                users
                            where 
                                uid=%s 
                            and 
                                upw=%s
                            ;
                        '''
                # 3-3. 쿼리 수행
                cursor.execute( sql, (uid, upw) )
                # 3-4. 결과 처리및 커서 닫기
                row = cursor.fetchone()
                # rows에서 하나씩 뽑아서 출력
                #print( row['name'] )
                # for row in rows:
                #     # 이름을 출력하시오
                #     print( type(row), row['name'] )
            # =====================================================
        except Exception as e:
            row = None
            print('에러->',e)
        else:
            print('정상수행')
        finally:
            # 4. 접속 종료
            print('연결종료')
        # 결과 리턴
        return row

    # 10년지 주식 정보를 가져온다 (종목코드, 언제부터 언제까지 10년치중 최신10개)
    # 최신10개만 가져온다
    def select_tradeLastData(self):
        rows = None # 쿼리 결과        
        try:            
            with self.conn.cursor() as cursor:
                sql    = 'select * from tbl_codehistory order by Date desc limit 10;'            
                cursor.execute( sql )
                rows   = cursor.fetchall()
        except Exception as e:
            rows = None
            #print('에러->',e)        
        # 결과 리턴
        return rows

    # 종목의 이름으로 종목 검색
    def select_searchTradeCode( self, tradeName ):
        rows = None # 쿼리 결과        
        try:            
            with self.conn.cursor() as cursor:
                sql    = '''
                        select code, name, cur from tbl_trade
                        where name like '%{0}%';
                        '''.format(tradeName)
                cursor.execute( sql )
                rows   = cursor.fetchall()
        except Exception as e:
            rows = None
            #print('에러->',e)        
        # 결과 리턴
        return rows

    # 종목 정보 가져오기
    def select_tradeInfo( self, code ):
        rows = None # 쿼리 결과
        rows2 = None        
        try:            
            with self.conn.cursor() as cursor:
                sql    = 'select * from tbl_trade where code=%s;'
                cursor.execute( sql, (code,) )
                rows   = cursor.fetchone()

                sql    = '''
                    select * from tbl_codehistory 
                    where code=%s
                    order by Date desc
                    limit 0, 10;
                '''
                cursor.execute( sql, (code,) )
                rows2   = cursor.fetchall()
        except Exception as e:
            rows = None
            rows2 = None
            #print('에러->',e)        
        # 결과 리턴 : 튜플로 리턴 => 리턴할 내용을 열거하면 된다
        return rows, rows2

    # 종목 정보 수정
    def update_tradeInfo( self, param ):
        result = None # 쿼리 결과        
        try:
            with self.conn.cursor() as cursor:
                sql    = '''
                        update tbl_trade set cur=%s, rate=%s where code=%s;
                        '''
                # param은 dict다
                cursor.execute( sql, (param['cur'],param['rate'],param['code']))
            # 최종 디비에 반영하게 하기 위해 커밋 진행 
            self.conn.commit()
            # 결과 > Affected rows 획득
            result = self.conn.affected_rows()
        except Exception as e:
            result = None
            #print('에러->',e)        
        # 결과 리턴
        return result

# 함수 테스트
if __name__ == '__main__':
    mgr = DBMgr()
    print( mgr.select_data() )