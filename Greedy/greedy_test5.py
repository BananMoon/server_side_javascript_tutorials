# <문제> 한 마을에 모험가가 N명 있습니다. 모험가 길드에서는 N명의 모험가를 대상으로 '공포도'를 측정했는데, '공포도'가 높은 모험가는
# 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어집니다. 모험가 길드장은 모험가 그룹을 안전하게 구성하고자 
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했습니다.
# 길드장은 최대 몇 개의 모험가 그룹을 만들 수 있는지 궁금합니다. N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하세요.
# 입력 : 5             출력 : 2
#        2 3 1 2 2 
# 몇명의 모험가는 마을에 그대로 남아있어도 되기 때문에, 모든 모험가를 특정한 그룹에 넣을 필요는 없습니다.

# 정리하면, 공포도가 2인 모험가는 반드시 2명 이상의 모험가 그룹에 참여해야한다!
# 예) 2 3 1 2 2
# 1. 오름차순 정렬 : 1 2 2 2 3
# 2. 앞에서부터 공포도 확인 
#  - 공포도 1은 혼자 그룹 결성 가능
#  - 공포도 2는 2,2 함께 그룹 경성
#  - 공포도 2, 3은 그룹 결성 안되므로 놔둠.
# 오름차순 정렬을 함으로써 항상 최소한의 모험가 수만 포함하여 그룹을 결성하게 됨

ppl = int(input())
# hor = [] 대신에
hor = list(map(int, input().split()))
cnt = 0 # 그룹의 수
mem = 0 # 그룹 내 모험가 수


# 공포도값으로 오름차순 정렬 [1, 2, 2, 2, 3]
hor.soted()
for i in hor: # 공포도값에 하나씩 접근
    mem = mem + 1 # 그룹에 모험가 포함시키기
    if i <= mem: # 현재 모험가의 공포도가 현재 그룹내 모험가 수보다 같거나 작으면
        cnt = cnt + 1 # 그룹 결성
        mem = 0  # 그룹 내 모험가 수 초기화
print(cnt)
