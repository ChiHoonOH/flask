title=None
while not title:
    title=input('게임의 제목 입력: ')
    #if not title:
    if len(title)>25:
        print('오류')
        title=None

print('''    
=================
= {} ==
= v1.0.0    ==
=================
'''.format(title))

while not gamer:
    gamer=input('게이머의 이름을 입력하세요.')
    if not gamer:
        print('아무것도 입력하지 않았습니다.')

