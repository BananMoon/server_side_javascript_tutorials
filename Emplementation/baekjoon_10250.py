# https://www.acmicpc.net/problem/10250 
# <분류>  구현, 사칙연산, 수학

T = int(input())

for t in range(T):
    H, W, N = map(int,input().split()) # 전체층수, 전체 호수, 방문 순서
    floor = N % H # 손님이 사용할 층수
    ho =  N // H +1 # 나머지가 0일 때 1호실이니까 +1을 해줘야함
    # 예외 - 높이가 딱 맞아 떨어질 때 
    if floor == 0:
        ho -= 1
        floor = H # 0이 아닌 가장 꼭대기층!
    print(floor*100+ho) 
