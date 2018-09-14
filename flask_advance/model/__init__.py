'''
-sql에 파라미터를 전달하여 일반화하기 (누구나 사용 할 수 있도록)
'''
#1.모듈 가져오기 : mysql 계열 RDBMS 제품을 쿼리하는 모듈
import pymysql as my

#2. 데이터베이스 접속
#IO의 기본은 예외처리
#10년치 주식 정보를 가져온다. (종목코드, 언제부터 언제까지 10년치 중 최신10개)
#최신 10개만 가져온다.
def select_tradeLastData():
    rows = None #쿼리 결과
    conn = None
    try:
        conn = my.connect(
            host = 'localhost',#127.0.0.1
            port = 3306, #기본포트가 3306이므로 변경하지 않았다면 생략
            user = 'root',
            password ='root',
            db ='pythondb',
            charset ='utf8',
            cursorclass = my.cursors.DictCursor
        )      
        with conn.cursor() as cursur:#cursor가 dictionary cursor            
            sql = '''
            select * from tbl_codehistory order by Date desc limit 10;
            '''            
            cursur.execute(sql)#return 값 없음.          
            rows = cursur.fetchall()         
  
    except Exception as e:
        rows = None         
    if conn:
        conn.close()      

    return rows #마지막에 적어준 이유는 close를 위해서 
#종목의 이름으로 종목 검색
def select_searchTradeCode(tradeName):
    rows = None #쿼리 결과
    conn = None
    try:
        conn = my.connect(
            host = 'localhost',#127.0.0.1
            port = 3306, #기본포트가 3306이므로 변경하지 않았다면 생략
            user = 'root',
            password ='root',
            db ='pythondb',
            charset ='utf8',
            cursorclass = my.cursors.DictCursor
        )      
        with conn.cursor() as cursur:#cursor가 dictionary cursor            
            sql = '''
            select code,name,cur from tbl_trade
            where name like '%{}%'
            ''' .format(tradeName)
             
            cursur.execute(sql)#return 값 없음.          
            rows = cursur.fetchall()         
  
    except Exception as e:
        rows = None         
    if conn:
        conn.close()      

    return rows
#종목 정보 가져오기
def select_tradeInfo(code):
    
    rows = None #쿼리 결과
    rows2 = None #쿼리 결과
    conn = None
    try:
        conn = my.connect(
            host = 'localhost',#127.0.0.1
            port = 3306, #기본포트가 3306이므로 변경하지 않았다면 생략
            user = 'root',
            password ='root',
            db ='pythondb',
            charset ='utf8',
            cursorclass = my.cursors.DictCursor
        )      
        with conn.cursor() as cursur:#cursor가 dictionary cursor            
            sql = '''select * from tbl_trade where code =%s;'''              
            cursur.execute(sql,(code,))#return 값 없음.          
            rows = cursur.fetchone() 

            sql = '''select * from tbl_codehistory
                where code=%s
                order by Date desc
                limit 0,10;          
            '''              
            cursur.execute(sql,(code,))#return 값 없음.          
            rows2 = cursur.fetchall() 
    except Exception as e:
        rows = None
        rows2 = None         
    if conn:
        conn.close()      
    
    return rows,rows2        #결과 리턴 : 튜프로 리턴 => 리턴할 내용을 열거

    def select_searchTradeCode(tradeName):
        rows = None #쿼리 결과
    conn = None
    try:
        conn = my.connect(
            host = 'localhost',#127.0.0.1
            port = 3306, #기본포트가 3306이므로 변경하지 않았다면 생략
            user = 'root',
            password ='root',
            db ='pythondb',
            charset ='utf8',
            cursorclass = my.cursors.DictCursor
        )      
        with conn.cursor() as cursur:#cursor가 dictionary cursor            
            sql = '''
            select code,name,cur from tbl_trade
            where name like '%{}%'
            ''' .format(tradeName)
             
            cursur.execute(sql)#return 값 없음.          
            rows = cursur.fetchall()         
  
    except Exception as e:
        rows = None         
    if conn:
        conn.close()      

    return rows
#종목 정보 가져오기
def update_tradeInfo(param):
    
    result = None #쿼리 결과
    
    conn = None
    try:
        
        conn = my.connect(
            host = 'localhost',#127.0.0.1
            port = 3306, #기본포트가 3306이므로 변경하지 않았다면 생략
            user = 'root',
            password ='root',
            db ='pythondb',
            charset ='utf8',
            cursorclass = my.cursors.DictCursor
        )      
        with conn.cursor() as cursur:#cursor가 dictionary cursor                        
            
            sql = '''update tbl_trade set cur=%s,rate=%s 
where code=%s;'''
            #param은 dict이다.                    
            cursur.execute(sql,(param['cur'],param['rate'],param['code'] ))#return 값 없음. 
            #최종 디비에 반경하기 위해 커밋 진행        
        conn.commit()
        
        #결과 > Affected rows 획득
        result = conn.affected_rows()
        
          
    except Exception as e:
        result = None
        print('->', e)
    if conn:
        conn.close()      
    
    return result
  
    
    



if __name__=='__main__':
    #if rows:#왜 에러냐
        # None, [] ,{},(),0, ''=>false
    #print('10년치 주식 정보 10개만 확인',select_tradeLastData())
    #print('10년치 주식 정보 10개만 확인',select_searchTradeCode('삼성'))
    #print(select_searchTradeCode('삼성'))
    
    #print(select_tradeInfo('005930')[0])
    #print('='*50)
    #print(select_tradeInfo('005930')[1])##이거 안나옴
    dic={'code':'005930','cur':'85,30121','rate':'3,10121'}
    print(update_tradeInfo(dic))

    