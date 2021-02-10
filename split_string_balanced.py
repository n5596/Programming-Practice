#https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        n = len(s)
        l = [0]*n
        r = [0]*n
        ll = 0
        rr = 0
        for i in range(n):
            c = s[i]
            if c == 'L':
                ll += 1
            elif c == 'R':
                rr += 1
            l[i] = ll
            r[i] = rr
        
        count = 0
        for i in range(n):
            if l[i] == r[i]:
                count += 1
        return count
