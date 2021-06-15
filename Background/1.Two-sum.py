# leetcode 1. Two-sum
# https://leetcode.com/problems/two-sum/
# 1. 완전탐색 유형(Brute-Force) : 모든 조합을 더해서 일일이 확인해보는 무차별 대입 방식 : 비효율적인 풀이법으로 첫 풀이로 자주 등장함
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)-1):
                if (target == nums[i]+nums[j]):
                    return [i,j]
        
# 2. in 이용한 탐색
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):  # 인덱스와 값
            complement = target - n
            
            if complement in nums[i+1:]:
                return [nums.index(n), nums[i+1:].index(complement) + (i+1)] # nums[i+1:]에서 인덱스는 0이니까 원래 리스트의 인덱스를 return해야하므로 (i+1)
        
# 3. 첫번째 수를 뺀 결과 키 조회 - 시간 복잡도를 개선
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i
            
        for i, num in enumerate(nums):
            # 필요한 추가 값이 nums_map에 있고, 필요한 추가값의 인덱스가 현재 값의 인덱스와 다르면 (즉 자기자신이 아니면)
            if (target - num in nums_map) and (i != nums_map(target - num):
                return [i, nums_map[target-name]]
                
# 4. 조회 구조 개선 - 약간의 성능향상과 간결한 코드
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target-num], i]
            nums_map[num] = i  #처음엔 아무것도 없으니, 1번째 값의 index와 값을 저장. 
        # 맞는 값이 있는지 찾아보면서 리스트에 하나씩 값을 저장하는걸 동시에 진행
        
                                               
# 아래의 투 포인터를 쓸 수 없는 이유? 우선 리스트를 정렬해야 한다. 근데, 리스트를 정렬하면 인덱스가 꼬인다.                
# 5. 투 포인터 이용 (투 포인터: 왼쪽 포인터와 오른쪽 포인터의 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로, 작다면 왼쪽 포인터를 오른 쪽으로 옮김)- 시간복잡도 O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        while not left == right:
            if left + right < target:  # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
                left += 1                                   
            else if left + right > target:  # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
                right -= 1
            else:
                return [left, right]  
