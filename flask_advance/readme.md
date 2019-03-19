## [[프로젝트 개요]]
###1.주식 데이터 리스트 처리 및 검색
-jinja를 이용한 테이블 표시
-javascript를 이용한 클라이언트 처리
-jquery 사용
-query가 추가(select,insert,update)
-ajax를 이용한 비동기통신 (클라이언트)
-json 처리
-디비사용 : 035510_주식_10년치데이터.sql

###2.프로젝트 구조
-run.py : 프로젝트 시작점
-templates : html 파일 위치
-static : 정적인 파일 위치(ex 업로드된 파일- 다른 곳일 수도 있음), *.js,*.css,*png
-model : 디비 관련 파일들

###3.필요 모듈 설치
-웹 구성
 > pip install flask
-디비 처리
 > pip install pymysql
 
