# 삼항 연산자 대체 처리
# 타언어 : 조건 ? 참일때값 : 거짓일때값
# 파이썬은 대체로 처리
try_count = 11
# point = (10-총시도횟수)*10점 단, 결과값이 0보다 작으면 다 0이다.

# A and B or C -> A가 참이면 B로 가고 거짓이면 B는 제끼고 C로 감.
# A and B  : A가 거짓이면 무조건 False이므로 B는 따지지 않는다.
# A or B => A가 참이면 무조건 true이므로, B는 따지지 않는다.
print('=>{0}'.format(try_count<10 and (10-try_count)*10 or 0))# 0 은 조건식에서 false

#if ~else
print('=>{0}'.format((10-try_count)*10 if try_count<10 else 0 ))# 0 은 조건식에서 false

#원래대로
point = 0
if try_count<10:
    point=(10-try_count)*10
#else면 무조건 0이므로 별도 표현 안함(초기값이 0이여서)    
print(point)
