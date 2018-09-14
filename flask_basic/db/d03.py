'''
-cursor를 닫는 부분은 간혹 잊어버리는 경향이 있다.
-장기적으로 디비 세션 획득에 오류를 유발 할 수 있다.
-알아서 닫히게 처리하자. => with ~ =>I/O

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
        port=3306, #기본포트가 3306이므로 변경하지 않았다면 생략
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
    with conn.cursor() as cursur:
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
        rows = cursur.fetchall()#이때 결과는 tuple이다.
        #rows에서 하나씩 뽑아서 출력
        print(type(rows),rows)        
        for element in rows:
            print(element)
            #이름을 출력하시오.
            print(element[3])
            
    #==========================

#4. 접속 종료
finally:
    if conn:
        conn.close()
        print('연결종료')
    else:
        print('오류로 인한 종료')