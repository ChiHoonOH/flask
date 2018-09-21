from random import randrange
gameTitle=None
gamer=None
while True:
    gameTitle = input('게임의 제목 입력(최대 28자,반드시 입력):')

    if not gameTitle:
        print("아무것도 입력하지 않았습니다.\n")
        continue
    if len(gameTitle) > 28:
        print('입력하신 %s는 28자를 초과하였습니다.\n' % gameTitle)
        continue
    #정상
    break
version='v1.0.0'
msg = '''
{0}
={1:^26}=
={2:^26}=
{3}
'''.format('='*28,gameTitle,version,'='*28)

#0:<10 0:>10 자릿수를 정해주고 정렬을 해준다.
print(msg)

#게임 시작


    #게이머의 이름을 입력 받는다.
while not gamer:
    gamer=input('게이머의 이름을 입력하세요.')
    if not gamer:
        print('아무것도 입력하지 않았습니다.')

print('%s 님 반갑습니다.'% gamer)

while True:
    number=input('0~99사이의 값을 예측하여 입력하세요: ')
    #정규 표현식
    #예외처리
    #말고는 모르겠는데..
    #if isinstance()
    #int(number)
    if number.isspace():
        print('공백오류')
        print('잘못된 값입니다. 다시 입력해주세요.')
        continue
    if number.isnumeric():        
        print('잘못된 값입니다. 다시 입력해주세요.')
        continue
    if number<0 or number>99:
        print('잘못된 값입니다. 다시 입력해주세요.')
        continue
    nansu=randrange(0,100)
    iterator=0
    while(nansu!=number):
        if nansu>number:
            print("값이 작습니다.")
            iterator+=1
        elif nansu<number:
            print("값이 큽니다.")
            iterator+=1
    print('총 {}번만에 맞추셨습니다.')
    iterator = 0
    lat = 'y'
    while lat == 'y' or lat == 'n':
        lat=input('게임을 다시 하시겠습니까?(y/n)')
        if not lat == 'y' or lat == 'n':            
            print('잘못된 입력 입니다.')
    
    break
        
        


    

    




    