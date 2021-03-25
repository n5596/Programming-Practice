#https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        top = 0
        for i in S:
            if i == '(':
                stack.append(i)
                top += 1
            elif i == ')' and top > 0 and stack[top-1] == '(':
                stack.remove(stack[top-1])
                top -= 1
            else:
                stack.append(i)
                top += 1
        return top
