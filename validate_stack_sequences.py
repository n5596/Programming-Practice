#https://leetcode.com/problems/validate-stack-sequences/

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0 
        j = 0
        n = len(pushed)
        m = len(popped)
        if n != m:
            return False
        while i < n or j < m:
            if len(stack)>0 and stack[-1] == popped[j]: #pop
                j+=1
                stack.pop()
            else:
                if i < n:
                    stack.append(pushed[i])
                    i += 1
                else:
                    break
        
        if len(stack) != 0:
            return False
        return True
