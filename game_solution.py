import pickle as p
import os
import operator
#print( "게임의 제목 입력" )
gameTitle = None
gamer     = None
gamer_dic={}
Total_score = 0
while True:
  gameTitle = input("게임의 제목 입력 (최대 28자 이내로 입력) : ")
  # 입력하지 않고 엔터를 치면 오류를 출력하고 다시 입력을 요청한다.
  #if len(gameTitle) == 0: # 문자열의 길이가 0이면 == 입력하지 않고 엔터를 치면
  if not gameTitle:# 입력하지 않고 엔터를 치면 == 빈값 => 조건식 False
    print( '아무것도 입력하지 않았습니다.\n' )
    continue
  # 최대 28자를 초과하였는가?
  if len(gameTitle) > 28:
    print( '입력하신 "%s"는 28자를 초과하였습니다.\n' % gameTitle )
    continue
  # 정상
  break

#5) 입력을 받으면 아래처럼 정렬하여 출력
# 게임 제목을 가운데 배치
# 관련 문법 : 여러줄 문자열 표시, 문자열 포멧팅, 문자열 치환식
if not gameTitle:
  # 프로세스 종료
  print(' 게임 타이틀이 없어서 종료함 ')
  import sys
  sys.exit()

msg = '''
{0}
={1:^28}=
={2:^28}=
{3}
'''.format('='*30, gameTitle,'v1.0.0', '='*30)
print ( msg )

while not gamer:
  # 6) 게이머의 이름을 입력받는다 
  gamer = input( '게이머의 이름을 입력하세요' )
  #(프럼프트:게이머의 이름을 입력하세요)
  # 7) 입력않하면 오류
  if not gamer:
    print('이름을 입력하지 않았습니다.')

# 게이머의 점수를 로드( 혹은 초기화)해서 표시하기
save_name = 'game.dat'
saveGameData={}
if os.path.exists( '%s\\%s' % (os.getcwd(),save_name)):
    with open('game.dat','rb') as f:
        saveGameData = p.load(f)
        #내가 처음으로 게임을 한 사람ㅇ ㅣ아니어서 내 아이디로 저장된 게임 데이터가 없을수 있음.
        if not gamer in saveGameData: # 내생각 saveGameData[gamer]:
            saveGameData[gamer]=0
            with open(save_name,'wb') as f:
              p.dump(saveGameData,f,p.HIGHEST_PROTOCOL)             
else:
    data=saveGameData[gamer]=0
    with open(save_name,'wb') as f:
        p.dump(saveGameData,f,p.HIGHEST_PROTOCOL)
        
print('%s 님 방갑습니다. 당신의 점수는 =%s' % (gamer,saveGameData.get(gamer)))  

## 게임 시작 #######################################
'''
8) 게임시작
9) (프럼프트:0~99사이의 값으만 AI의 값을
    예측하여 입력하세요) 
10) 공백을 넣으면 오류 -> 9번 이동
11) 숫자가 아니면 오류 -> 9번 이동
12) 값의 범위를 넘으면 오류 -> 9번 이동
'''
# 더미 값 임시 입력 -> 개발간 반복 작업 제거
#gameTitle   = 'number game'
#gamer       = 'player'
match_value = None  # 사용자 입력값
comp_value  = None  # 컴퓨터 생성값
try_count = 0 # 시도 횟수
isGamePlay = True # True : 게임 진행중, False : 게임종료 =>flag 변수

while isGamePlay:
  match_value = 0
  comp_value = 0
  try_count = 0 # 시도 횟수
  while True:
    while True:
      user_input = input('프럼프트:0~99사이의 값으만 AI의 값을 예측하여 입력하세요')
      
      # 양쪽 공백 제거
      user_input = user_input.strip()
      # 공백을 넣으면 오류 -> 9번 이동
      if not user_input:
        print('아무것도 입력하지 않았습니다. ')
        continue
      # 숫자가 아니면 오류 -> 9번 이동
      # if A and B
      # 1로 않하고 [1 ], [ 1], [1 2]
      # 특수문자는 통과가 되었으니 체크 필요
      elif user_input.isalpha() and not user_input.isdecimal():
        print('숫자를 입력하지 않았습니다. ')
        continue
      # 값의 범위를 넘으면 컷 -> 9번 이동
      # 문자를 정수로
      match_value = int(user_input)
      # 0~99사이를 넘으면 다시
      if 0>match_value or match_value>99:
        print('값의 범위를 넘어 섰습니다. 0~99까지 값으로 다시 입력')
        continue
      # 정상 입력
      break
    print('사용자 입력 완료 %d' % match_value)
    #시도 횟수 증가
    try_count += 1
    # 컴퓨터가 0~99사이의 값중 임의값을 하나 생성
    import random
    # 0 ~ 99
    if not comp_value:#최초 1회만 세팅되고 넘어감.
      comp_value = random.randint(0,99)

    # 13) 값이 작으면 작다고 출력하고 다시 입력받음
    if match_value < comp_value:
      print( "입력값이 작습니다." )
      continue # 60라인으로 점프
    # 14) 값이 크면 크다고 출력하고 다시 입력받음
    elif match_value > comp_value:
      print( "입력값이 큽니다." )
      continue # 60라인으로 점프
    else:
      # point = (10 - 총시도 횟수) * 10 
      point = (11 - try_count) * 10 
      if point<0:
            point = 0
      # 점수 누적
      saveGameData[gamer] += point    
      # 점수를 저장소에 반영(부분만 갱신 등등 이런 부분 배제)  
      # 다른 사람이 혹시 그 사이에 값이 변경되었다라는 부분은 배제함(취지를 벗어남)
      with open(save_name,'wb') as f:
        p.dump(saveGameData, f, p.HIGHEST_PROTOCOL)
      print('''
        정답입니다. 게이머 입력값={}, AI값={}
        {name}님의 총 시도 횟수 {count}입니다.
        획득 점수는 {point}입니다.        
      ''' .format(match_value, comp_value, name = gamer, count = try_count, point = point,Total_score = Total_score))          
       
      break
  #게임 한판이 종료 ->다시하시겠습니까?
  
  while True:
        #공백 제거, 사용자가 대소문자 섞던 말던 무조건 대문자로 체크
    res = input('다시하시겠습니까?(yes/no)').strip().upper()
    if res == 'YES':
      break
    elif res == 'NO':
      isGamePlay = False
      break
    else:
      print('정학하게 yes or no를 입력하세요.')   

print('game over')
def dkanrjks(number):
      return number[1]
with open(save_name,'rb') as f:
    temp=p.load(f)
    result = sorted(temp.items(),key=lambda number:number[1],reverse=True)
    print('='*25)
    for element in result:                
      print('{0:<10}'.format(element[0]),'{0:>10}'.format(element[1]))
    print('='*25)
    
import sys
sys.exit()

# 최초 파일이 없었을때 오픈해서 읽어오든지, 만들던지

# 게임 시작을 하면 플레이어 이름에 맞춰서 저장된 점수를 가져와야한다.
# 플레이어 별로 점수 저장
# 누적 점수 합산하여 결과 때 표기
# 게임 종료시 플레이어별 점수 소트하여 표시