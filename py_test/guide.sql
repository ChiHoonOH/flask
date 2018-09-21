-- db접속
-- mysql [-u 사용자명] [-p] [-h host] [데이터베이스]
mysql -u root -p
password:root
-- prompt
-- 마리아 데이터베이스를 실제 접속 했다.
MariaDB[(데이터베이스명)] 

-- 데이터베이스 보여주기
show databases;

--데이터베이스선택
use pythondb;


--데이터베이스 생성
create database my_db;
create database if not exists my_db;

-- sql: 데이터베이스와 소통하기 위한 최적화된 언어이다.(structed query language).

-- 데이터베이스 삭제
drop database my_db;
drop database if exists my_db;

-- 데이터베이스 목적
-- 데이터 저장 => 테이블 => row + colume 2차원 구조
-- row : 레코드, 레코드에 있는 데이터들은 컬럼 구분
-- 여러 테이블들이 하나 이상 관계를 가질 수 있다. 
-- --> 관계형데이터베이스
-- 테이블을 정의하고, 여러테이블을 나누는 과정 -> 정규화

