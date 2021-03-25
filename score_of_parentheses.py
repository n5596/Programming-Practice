#https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        n = len(S)
        lst = []
        for i in S:
            lst.append(i)
        
        while len(lst) != 1:
            for i in range(len(lst)):
                if i<len(lst)-1 and lst[i] == '(' and lst[i+1] == ')':
                    lst[i] = 1
                    lst.pop(i+1)
            for i in range(len(lst)):
                if i < len(lst)-1 and lst[i] != '(' and lst[i] != ')' and lst[i+1] !='(' and lst[i+1] != ')':
                    lst[i] = lst[i]+lst[i+1]
                    lst.pop(i+1)
            for i in range(len(lst)):
                if i < len(lst)-2 and lst[i] == '(' and lst[i+2] == ')' and lst[i+1] != ')' and lst[i+1] != '(':
                    lst[i] = 2*lst[i+1]
                    lst.pop(i+1)
                    lst.pop(i+1)
        return lst[0]
