# 상하좌우 문제
# - 여행가 A는 NxN 크기의 정사각형 공간 위에 서있음
# - 현재 위치 및 시작 좌표는 항상 (1,1)
# - 여행가 A가 이동할 계획이 적힌 계획서가 놓여있음
# - 입력은 띄어쓰기를 기준으로 L R U D 중 문자가 반복적으로 적혀있음 
# (L : 왼쪽 한칸 이동, R: 오른쪽 한칸 이동, U : 위로 한칸 이동, D : 아래로 한칸 이동)
# - 정사각형 공간을 벗어나는 움직임은 무시됨
# 예시: N=5인 지도와 계획서(R-R-R-U-D-D)

# 이 문제는 요구사항대로 충실히 "구현"하면 되는 문제
# 일련의 명령에 따라 개체를 차례로 이동시키는(시뮬레이션) 유형

# <생각 정리> 우선적으로, 현재 위치, 이동가능한 방향(동서남북)에 대해 선언해준 후에, 입력으로 받은 방향이 동서남북 중 일치하는 방향으로 이동시킨다.
# 단, 이동한 위치는 범위를 벗어나면 안된다.

# <코드>
n = int(input())
plans = input().split()  # R R R U D D,  list로 안하고 string으로 해도 됨

x, y = 1, 1
dirx = [0, -1, 0, 1] # 동, 북, 서, 남
diry = [1, 0, -1, 0]
move_types = ['R', 'U', 'L', 'D']

for plan in plans:
  # 한 개의 이동계획에 대해 4가지 모두 확인
  for i in range(len(move_types)):
    if plan == move_types[i]:
      newx = x + dirx[i] # 다음 위치값
      newy = y + diry[i]
      
  if newx<1 or newy<1 or newx>n or newy>n: # 새로운 좌표가 (1,1) 보다 작거나 (n,n)보다 크면 범위를 벗어난 것!
      continue
  x, y = newx, newy
        
print(x, y)
