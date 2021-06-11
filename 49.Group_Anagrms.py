# leetcode 49. Group Anagrams
# https://leetcode.com/problems/group=anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 풀이 : 정렬하여 딕셔너리에 추가 (문자열을 정렬한 후 딕셔너리로 같은 문자열끼리 묶음)
        anagram = collections.defaultdict(list)
        
        for word in strs:
            anagram[''.join(sorted(word))].append(word)  #  sorted('eat')는 결과를 list ['a', 'e', 't']로 출력하므로 join으로 다시 합쳐줘야 딕셔너리의 key값으로 사용 가능함!
            # eat를 정렬한 aet에 eat 추가. tea를 정렬한 aet에 tea 추가 -> {'aet' : 'eat', 'tea'}
            
        return list(anagram.values())  # aet의 값(eat, tea)을 리스트로 출력
        
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Anagram(애너그램)이란?
# 일종의 언어유희. 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것
# 예) eat -> ate, tea
