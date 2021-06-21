# 삽입정렬의 기본적인 로직

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1,len(array)):
  for j in range(i, 0, -1):  # 거꾸로 강 맨 앞에 가장 작은 수가 놓임
    if array[j] < array[j-1]:
      array[j], array[j-1] = array[j-1], array[j]
    else:
      break # 다음 index 비교로 pass~

print(array)

# i가 1일때
# j 가 [1]vs[0] 비교
# i가 5일때
# j가 5~0 : [5]vs[4] [4]vs[3] [3]vs[2] [2]vs[1] [1]vs[0] 비교
