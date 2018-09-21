# 모둘 가져오기 : RDBMS 제품 mysql 계열을 쿼리하는 모듈
import pymysql as my

# 자료실 데이터 가져오기(페이징X)
def select_data():
    rows = None # 쿼리 결과
    conn = None
    try:
        conn = my.connect(
                    host='pythondb.c69gi2s1odpt.ap-northeast-2.rds.amazonaws.com', #'localhost',                    
                    user='root',
                    password='12341234',
                    db='pythondb',
                    charset='utf8',
                    cursorclass=my.cursors.DictCursor
                    ) 
        with conn.cursor() as cursor:
            sql    = 'select * from tbl_uplaodBbs order by id desc limit 0, 10; '            
            cursor.execute( sql )
            rows   = cursor.fetchall()
    except Exception as e:
        rows = None
        #print('에러->',e)
    if conn:conn.close()
    # 결과 리턴
    return rows

# 자료실 업로드 처리
def insert_data( title, contents, uid, fileUrl ):
    result = 0
    # ===========================================
    conn   = None
    try:
        conn = my.connect(
                    #host='127.0.0.1', #'localhost',                    
                    host='pythondb.c69gi2s1odpt.ap-northeast-2.rds.amazonaws.com', #'localhost',                    
                    user='root',
                    password='12341234',
                    db='pythondb',
                    charset='utf8',
                    cursorclass=my.cursors.DictCursor
                    ) 
        with conn.cursor() as cursor:
            sql    = '''
                    insert into tbl_uplaodBbs(title, contents, author, fileUrl, regdate) 
                    values ( %s, %s, %s, %s, now() );
                    '''
            cursor.execute( sql, (title, contents, uid, fileUrl))
        conn.commit()        
        result = conn.affected_rows()
    except Exception as e:
        result = 0
        #print('에러->',e)
    if conn:conn.close()
    # ===========================================
    return result

# flask_basic>db>d08.py에서 카피
def loginSql(uid, upw):
    row  = None # 쿼리 결과
    conn = None
    try:
        # 2. 데이터베이스 접속
        # 2-1 디비오픈
        conn = my.connect(
                    #host='127.0.0.1', #'localhost',
                    host='pythondb.c69gi2s1odpt.ap-northeast-2.rds.amazonaws.com', #'localhost',                    
                    #port=3306, #기본포트가 3306이므로 변경하지 않았으면생략
                    user='root',
                    password='12341234',
                    db='pythondb',
                    charset='utf8',
                    cursorclass=my.cursors.DictCursor
                    )
        # 3. 쿼리수행 ==========================================
            # 3-1. 커서 획득
        with conn.cursor() as cursor:
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
        if conn:
            conn.close()
            print('연결종료')
        else:
            print('오류로 인한 종료')
    # 결과 리턴
    return row

# 10년지 주식 정보를 가져온다 (종목코드, 언제부터 언제까지 10년치중 최신10개)
# 최신10개만 가져온다
def select_tradeLastData():
    rows = None # 쿼리 결과
    conn = None
    try:
        conn = my.connect(
                    #host='127.0.0.1', #'localhost',                    
                    host='pythondb.c69gi2s1odpt.ap-northeast-2.rds.amazonaws.com', #'localhost',                    
                    user='root',
                    password='12341234',
                    db='pythondb',
                    charset='utf8',
                    cursorclass=my.cursors.DictCursor
                    ) 
        with conn.cursor() as cursor:
            sql    = 'select * from tbl_codehistory order by Date desc limit 10;'            
            cursor.execute( sql )
            rows   = cursor.fetchall()
    except Exception as e:
        rows = None
        #print('에러->',e)
    if conn:conn.close()
    # 결과 리턴
    return rows

# 종목의 이름으로 종목 검색
def select_searchTradeCode( tradeName ):
    rows = None # 쿼리 결과
    conn = None
    try:
        conn = my.connect(
                    #host='127.0.0.1', #'localhost',                    
                    host='pythondb.c69gi2s1odpt.ap-northeast-2.rds.amazonaws.com', #'localhost',                    
                    user='root',
                    password='12341234',
                    db='pythondb',
                    charset='utf8',
                    cursorclass=my.cursors.DictCursor
                    ) 
        with conn.cursor() as cursor:
            sql    = '''
                    select code, name, cur from tbl_trade
                    where name like '%{0}%';
                    '''.format(tradeName)
            cursor.execute( sql )
            rows   = cursor.fetchall()
    except Exception as e:
        rows = None
        #print('에러->',e)
    if conn:conn.close()
    # 결과 리턴
    return rows

# 종목 정보 가져오기
def select_tradeInfo( code ):
    rows = None # 쿼리 결과
    rows2 = None
    conn = None
    try:
        conn = my.connect(
                    #host='127.0.0.1', #'localhost',                    
                    host='pythondb.c69gi2s1odpt.ap-northeast-2.rds.amazonaws.com', #'localhost',                    
                    user='root',
                    password='12341234',
                    db='pythondb',
                    charset='utf8',
                    cursorclass=my.cursors.DictCursor
                    ) 
        with conn.cursor() as cursor:
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
    if conn:conn.close()
    # 결과 리턴 : 튜플로 리턴 => 리턴할 내용을 열거하면 된다
    return rows, rows2

# 종목 정보 수정
def update_tradeInfo( param ):
    result = None # 쿼리 결과
    conn   = None
    try:
        conn = my.connect(
                    #host='127.0.0.1', #'localhost',                    
                    host='pythondb.c69gi2s1odpt.ap-northeast-2.rds.amazonaws.com', #'localhost',                                       user='root',
                    password='12341234',
                    db='pythondb',
                    charset='utf8',
                    cursorclass=my.cursors.DictCursor
                    ) 
        with conn.cursor() as cursor:
            sql    = '''
                    update tbl_trade set cur=%s, rate=%s where code=%s;
                    '''
            # param은 dict다
            cursor.execute( sql, (param['cur'],param['rate'],param['code']))
        # 최종 디비에 반영하게 하기 위해 커밋 진행 
        conn.commit()
        # 결과 > Affected rows 획득
        result = conn.affected_rows()
    except Exception as e:
        result = None
        #print('에러->',e)
    if conn:conn.close()
    # 결과 리턴
    return result

# 함수 테스트
if __name__ == '__main__':
    #print( '10년치 주식 정보 10개만 확인->', select_tradeLastData() )
    #print( select_searchTradeCode('삼성') )
    #print( select_tradeInfo('005930')[0] )
    #print( '='*50)
    #print( select_tradeInfo('005930')[1] )
    # 수정 테스트 (원래값->수정값->없는코드를 사용해서)
    dic = { 'code':'00066', 'cur':'85,301', 'rate':'3,101' }
    print( update_tradeInfo(dic) )