#https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            idx = abs(nums[i])-1
            e = nums[idx]
            #print(idx, e)
            if e >= 0: #not encountered before
                nums[idx] *= -1
            else:
                #print(e, idx, i, nums[i])
                ans.append(abs(nums[i]))
        return ans
