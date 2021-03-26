#https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        if s == "":
            return 0
        stack = [s[0]]
        cstack = [cost[0]]
        
        count = 0
        for i in range(1,len(s)):
            l = s[i]
            if len(stack) > 0 and l == stack[-1]:
                count += min(cstack[-1], cost[i])
                if cstack[-1] < cost[i]: #replace
                    cstack.pop()
                    cstack.append(cost[i])
            else:
                stack.append(l)
                cstack.append(cost[i])

        return count
