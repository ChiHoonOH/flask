# 딕셔널 ㅣ정렬
# 딕셔너리 =>순서가 없다. 키 : 값으로 구성, 키는 고유, 값은 중복되고 OK
# 키나 값은 기본적으로 어떤 값이 와도 관계 없음

import collections
import operator
data = {'부산대':0, '온천장':40, '서면':20}
print(data.items())
print(data.keys())
print(data.values())
dic = collections.OrderedDict(sorted(data.items()))#키를 중심으로 가나다
for k,v in dic.items():
    print(k,v)
print()
#오류
#키가 없어서 OrderedDict()에 입력이 불가능함.
dic = collections.OrderedDict(sorted(data.items(),key=operator.itemgetter(1),reverse=True))
dic = collections.OrderedDict(sorted(data.items(),key=lambda number:number[1],reverse=True))


for k,v in dic.items():
    print(k,v)


