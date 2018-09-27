from random import randrange
# gameTitle=None
# gamer=None
# while True:
#     gameTitle = input('게임의 제목 입력(최대 28자,반드시 입력):')

#     if not gameTitle:
#         print("아무것도 입력하지 않았습니다.프로세스를 종료합니다.\n")
#         import sys
#         sys.exit()        
#     if len(gameTitle) > 28:
#         print('입력하신 제목은 28자를 초과하였습니다.\n')
#         continue
#     #정상
#     break
# version='v1.0.0'
# msg = '''
# {0}
# ={1:^26}=
# ={2:^26}=
# {3}
# '''.format('='*28,gameTitle,version,'='*28)

# #0:<10 0:>10 자릿수를 정해주고 정렬을 해준다.
# print(msg)

# #게임 시작


# #게이머의 이름을 입력 받는다.
# while not gamer:
#     gamer=input('게이머의 이름을 입력하세요.')
#     if not gamer:
#         print('아무것도 입력하지 않았습니다.')

# print('%s 님 반갑습니다.'% gamer)

#더미 값 임시 입력 => 개발간 반복작업 제거
gameTitle='number game'
gamer='player'

nansu=randrange(0,99)
iterator=1
while True:
    number = input('0~99사이의 값을 예측하여 입력하세요: ')
    number = number.strip() #양쪽 공백 제거
    #정규 표현식
    #예외처리
    #말고는 모르겠는데..
    #if isinstance()
    #int(number)
    
    if not number:        
        print('입력되지 않았습니다. 다시 입력해주세요.')
        continue
    #특수문자는 통과가 되었으니 체크 필요.
    if number.isalpha() and not user_input.isdecimal():
        print('숫자를 입력하지 않았습니다.')
        continue    
    if not number.isnumeric(): 
        print('숫자오류')       
        print('잘못된 값입니다. 다시 입력해주세요.')
        continue
    number = int(number)
    if number<0 or number>99:
        print('범위오류')
        print('잘못된 값입니다. 다시 입력해주세요.')
        continue
    
    
    
    if nansu>number:
        print("값이 작습니다.")
        iterator+=1
        continue
    elif nansu<number:
        print("값이 큽니다.")
        iterator+=1
        continue
    print('총 {}번만에 맞추셨습니다.'.format(iterator))
    iterator = 1
    lat = 'y'
    
    lat=input('게임을 다시 하시겠습니까?(y/n)')
    if not lat == 'y' or lat == 'n':            
        print('잘못된 입력 입니다.')
    if lat == 'y':
        continue
    
    break    