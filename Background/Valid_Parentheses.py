# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for char in s:
            if char not in table: # 닫는 괄호가 아니면 stack에 추가
                stack.append(char)
            elif not stack or table[char] != stack.pop(): # stack이 비어있거나, 마지막 원소가 일치하는 괄호가 아니라면
                return False
        return len(stack) == 0  # stack이 비었으면 True 리턴
        
        # 예) (([{}]))
        # (, (, [, { append
        # } : pop('{')
        # ] : pop('[')
        # ) : pop('(')
        # stack 비었음. -> return True
