#https://leetcode.com/problems/subsets/submissions/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        nums.sort()
        l = 0
        i = 0
        while l < len(nums):
            curr = ans[i]
            for j in nums:
                if j in curr:
                    continue
                v = copy.copy(curr)
                v.append(j)
                
                v.sort()
                if v in ans:
                    continue
                    
                ans.append(v)
            i += 1
            l = max(l, len(v))
            
        return ans
