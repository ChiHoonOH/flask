# 피클
# 구조화된 모듈 저장 및 로드
# 리스트 튜플, 딕셔너리 등등 =>저장 => 로드 => 리스트, 튜플, 딕셔너리
import pickle as p
data = {
1:[1,2,3,4],
2:{'gamer':100},
3:(5,6,7,8)
}
# 기록
with open('data.py','wb') as f:
    p.dump(data, f, p.HIGHEST_PROTOCOL) # p.HIGHEST_PROTOCOL 구조 저장
    

# 로드
with open('data.py','rb') as f:
    temp = p.load(f)
    print(temp)
