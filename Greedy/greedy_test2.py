# https://www.acmicpc.net/problem/5585
# baekjoon n.5585
# greedy algorithm practice..

money = 1000
cus = int(input())
back = money - cus
arr = [500,100,50,10,5,1]
count = 0

for coin in arr:
    if back >= coin: # 거슬러줘야할 돈이 coin보다 클 때만 실행
        count = count+ back//coin # 몫
        back = back%coin # 나머지
print(count)
