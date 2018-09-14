'''
python에서 mariadb(mysql 계열) 접속 쿼리 수행
- pip install pymysql
-I/O 작업 수행시 예외 처리 해야한다.
'''
#1.모듈 가져오기
import pymysql as my
# try:
#     pass
# except expression as identifier:
#     pass
# else:
#     pass
# finally:
#     pass
#2. 데이터베이스 접속
#IO의 기본은 예외처리
#2-1 디비오픈
conn = None
try:
    conn = my.connect(
        host = 'localhost',#127.0.0.1
        port = 3306, #기본포트가 3306이므로 변경하지 않았다면 생략
        user = 'root',
        password='r213213',
        db='pythondb',
        charset='utf8'
    )
except Exception as e:
    print(e)
    pass
else:
    print('정상수행')
#3. 쿼리수행

#4. 접속 종료
finally:
    if conn:
        conn.close()
        print('연결종료')
    else:
        print('오류로 인한 종료')