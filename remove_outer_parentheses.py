#https://leetcode.com/problems/remove-outermost-parentheses/
#Used stack data structure

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        top = -1
        ind = []
        for a in range(len(S)):
            b = S[a]
            if top == -1:
                stack.append(b)
                ind.append(a)
                top += 1
            else:
                if stack[top] == '(' and b == ')':
                    top -= 1
                elif stack[top] == ')' and b == '(':
                    top -= 1
                else:
                    stack.append(b)
                    top += 1
                if top == -1:
                    ind.append(a)
        #print(ind)
        final = ''
        for i in range(len(S)):
            if i not in ind:
                final = final + S[i]
        return final
