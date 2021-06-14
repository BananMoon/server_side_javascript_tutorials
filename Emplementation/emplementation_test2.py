# 시각 문제
# 00시 00분 00초에서 N시 59분 59초 사이의 모든 시각에서 3이 나타나는 경우의 수를 구하는 문제 (0 <= N <= 23)

# <생각 정리> 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제 -> 완전 탐색(Brute Forcing) 문제 (구현) 유형

n = int(input())  # 3이면 0~3시까지
time = 60
cnt = 0 # 경우의 수

for h in range(n+1):
  for m in range(time):
    for s in range(time):
      if '3' in str(h)+str(m)+str(s):   # 포함되어있는지를 세려면 문자열형태로 더해주고, 그 안에 3이 포함되어있는지 체크!
        cnt += 1
        
print(cnt) # n이 3이라면 8325 출력


# 오류) 13번 문장을 다음과 같이 나타내면 
#  if 3 in h or 3 in m or 3 in s: 
# -> TypeError: argument of type 'int' is not iterable
