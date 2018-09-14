'''
-데이터를 키(컬럼명)을 통해서 데이터를 획득하면
-데이터의 순서가 뒤바껴도 문제 없다 : 딕셔너리 => 순서x

'''
#1.모듈 가져오기
import pymysql as my
#2. 데이터베이스 접속
#IO의 기본은 예외처리
#2-1 디비오픈
conn = None
try:
    conn = my.connect(
        host = 'localhost',#127.0.0.1
        port= 3306, #기본포트가 3306이므로 변경하지 않았다면 생략
        user = 'root',
        password='root',
        db='pythondb',
        charset='utf8'
    )
except Exception as e:
    print(e)
    pass
else:
    print('정상수행')
    #3. 쿼리수행
    #3-1.커서 획득
    with conn.cursor(my.cursors.DictCursor) as cursur:#cursor가 dictionary cursor
        #3-2 sql 준비
        sql = '''
        select 
            * 
        from 
            users
        where 
            uid='bu'
        and 
            upw = '1234'
        '''
        #3-3 쿼리 수행
        cursur.execute(sql)#return 값 없음.
        #3-4 결과 처리
        rows = cursur.fetchall()
        
        #rows에서 하나씩 뽑아서 출력
        print(type(rows))
        for element in rows:
            print(element)        
            #이름을 출력하시오.
            print(element['name'])
            
    #==========================

#4. 접속 종료
finally:
    if conn:
        conn.close()
        print('연결종료')
    else:
        print('오류로 인한 종료')