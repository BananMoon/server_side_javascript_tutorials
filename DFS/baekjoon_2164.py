# https://www.acmicpc.net/problem/2164
# 백준 BFS 문제- 카드2

from collections import deque
n = int(input())
queue = deque()
   
for i in range(1, n+1): # 전체 카드를 큐에 넣음.
  queue.append(i)
while len(queue) > 1: # 1개 남을때까지
  queue.popleft()     # 1개는 버리고
  p = queue.popleft()
  queue.append(p)     # 1개는 밑으로 추가
    
print(queue.popleft())
