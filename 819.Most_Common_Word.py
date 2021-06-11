# leetcode 819. Most Common Word
# https://leetcode.com/problems/most-common-word/

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = []
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph) # 주의! ''가 아니고 ' '임. ''로 하게 되면, split()이 먹히지 않음..
                 .lower().split()
                    if word not in banned] 
         # 1.word character가 아닌 것은 ' '으로 변경 2.소문자로 치환 후, 단어 split 3.banned에 있지않은 단어만
         
        # 단어의 등장 갯수를 담아두는 딕셔너리 생성!        
#       counts = collections.defaultdict(int)
#       counts[word] +=1 # word가 key, int가 values
#       return max(counts, key=counts.get) # 딕셔너리 counts에서 빈도수가 가장 큰 단어를 가져옴
    
# 다만, 이보다는 개수를 처리하는 기능을 가지는 Counter 모듈을 이용해보자!
        counts = collections.Counter(words) # words에 있는 단어의 갯수들을 셀 수 있음.most_commons()로 뽑을 수도 있음
        return counts.most_common(1)[0][0] # 첫번째 문장의([0]) 단어만([0]) 추출
        
        
# input : "Bob hit a ball, the hit BALL flew far after it was hit."
          ["hit"]
# output : "ball
# words는 ["bob", "hit", "a", "ball", "the", "hit", "ball", "flew", "far", "after", "it", "was", "hit"]
