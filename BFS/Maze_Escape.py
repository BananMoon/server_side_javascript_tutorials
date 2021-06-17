def dfs(x,y):
  queue = deque()
  queue.append(x, y)

  while queue:
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      #공간을 벗어난 경우
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      # 벽인경우
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[nx][ny] + 1
        queue.append((nx, ny))
  return graph[n-1],[m-1]

from collections import deque

n, m = map(int, input().split())

graph = []
for _ in n:
  graph.append(list(map(int, input())))

# 갈 수 있는 방향. 상하좌우 (dx가 -1일 때 상!)
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

print(dfs(0, 0))
