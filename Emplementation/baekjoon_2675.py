# https://www.acmicpc.net/problem/2675
# 백준 2675번 문자열 반복

# 리스트로 안해도 됨. only string

n = int(input())
for i in range(n): # 테스트케이스 횟수
    text =''       # 문자열 미리 초기화
    num, s = input().split()  # 입력받음
    for j in s:    # 문자열에 하나씩 접근
        text += j*int(num)    # num만큼 곱해서 문자열에 추가 (* 이용)
    print(text)
