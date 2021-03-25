#https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di = {}
        for n in nums:
            if n in di:
                di[n] += 1
            else:
                di[n] = 1
        sort = sorted(di.values(), reverse=True)
        
        c = 0
        ans = []
        flag = 0
        
        for i in sort:
            for j in di.keys():
                if di[j] == i and j not in ans:
                    ans.append(j)
                    c += 1
                    if c == k:
                        flag = 1
                    break
            if flag == 1:
                break
        return ans
            
