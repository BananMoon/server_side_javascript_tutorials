# 링크 : https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    return sorted(strings, key = lambda x: (x[n],x))    

# 테스트 케이스
print(solution(["adcd","adce","adx"],2))

# 드디어 '다른 사람의 풀이'에서 첫번째로 나와있는 코드와 내 풀이가 같았다..

# 여기서 중요한 점
# 1. sorted()만 return하는데에 넣어주는게 가능
# why? sorted 함수와 달리 정렬 후 정렬된 리스트를 return 해주지 않기 때문
# 2. 'key = '으로 설정하는데 보통 lambda함수를 이용함
# 3. 정렬 조건을 2개 줄 경우, labmda x: (조건1, 조건2) 다음과 같이 적어줘야함.
