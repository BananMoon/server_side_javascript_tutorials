# <문제> 각 자리가 숫자(0~9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에
# 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오. 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.
# 입력 : 02984  출력 : 576
# facebook interview problem

strnum = input()
res = int(strnum[0])

for i in range(1,len(strnum)):
    num = int(strnum[i])
    if res <= 1 or num <= 1:  # 둘중에 하나라도 1이하인 경우, 더하기 수행
        res = res + num
    else:
        res = res * num
print(res)
