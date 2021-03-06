# 체육복 문제 (https://programmers.co.kr/learn/courses/30/lessons/42862)

# reserve는 여벌의 체육복, 중복x
# lost에 있는 학생이 reserve에도 있는 경우, 빌려줄수없음.
# 학생 전부의 리스트를 만들어본다.

def solution(n, lost, reserve):
    stu = [1]*n # n명의 학생들 리스트
    # reserve는 1(학생번호)부터, stu는 0부터니까
    # reserve의 i번째에서 1을 빼야함.
    for i in reserve:
        stu[i-1] = 2 # 여벌옷 가지고있는 학생은 2개 체육복 소유
    for i in lost:
        stu[i-1] = stu[i-1]-1 # 잃어버린 학생은 -1
        
    # 빌려주는 작업
    # enumerate는 index와 value를 동시에 가져올 수 있음.
    for i, v in enumerate(stu):
        # stu[i]==0의 앞 친구가 빌려주는 경우(i==0일때 앞 친구가 없으니까 x)
        if i>0 and v==0 and stu[i-1] ==2:
            stu[i]=1 # 체육복 획득
            stu[i-1] = 1 # 빌려주면 친구의 체육복은 -1
        # stu[i]==0의 뒷 친구가 빌려주는 경우(i==4일때 뒷 친구가 없으니까 x)
        # 학생수(인덱스니까-1)보다 적은 인덱스에서
        elif i<n-1 and v==0 and stu[i+1]==2: 
            stu[i]=1
            stu[i+1]=1
        
    # 체육복을 갖고 있는 학생들 세기(값이 0인 학생 수를 빼면 됨)
    return n-stu.count(0)
    
    
# 다른 사람의 풀이
# 정말 간결하게 잘 풀었다.
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]  # lost에 없는 reserve들
    _lost = [l for l in lost if l not in reserve]     # reserve에 없는 lost들
    for r in _reserve:                                # 2개씩 가지고 있는 학생들의 배열을 반복하면서
        f = r - 1                                     # 앞 친구
        b = r + 1                                     # 뒷 친구
        if f in _lost:                                # 앞 친구가 lost에 있는 친구면
            _lost.remove(f)                           # 빌려주고, lost에서 삭제
        elif b in _lost:                              # 뒷 친구가 lost에 있는 친구면
            _lost.remove(b)                           # 빌려주고, lost에서 삭제
    return n - len(_lost)                             # lost에 있는 친구들을 제외한 학생 수 return
