import sys

tests = int(input())
for test in range(tests):
    cnt = 1 # 1위
    grade = []

    peoples = int(input()) # 신입사원 수

    for i in range(peoples):
        paper, interview = map(int, sys.stdin.readline().split())
        grade.append([paper, interview])

    grade.sort() # 서류 순위 기준 정렬
    Min = grade[0][1]

    for i in range(1, peoples):
        if Min > grade[i][1]:
            cnt = cnt+1
            Min = grade[i][1]

    print(cnt)


# 서류 순위 기준으로 오름차순정렬한 후에
# 면접 순위를 비교하는데, min과 비교하면서 해야해. min이랑 비교했을 때 min보다
# if) 면접 순위가 높다면 (작다면) 합격수(cnt)+, else) 서류순위도 낮으면 탈락..(cnt 추가 안한단 의미)

# 변수 하나, 위치 하나에도 신경써서 처음부터 꼼꼼히 해야겠다
