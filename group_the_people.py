#https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/submissions/

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        n = len(groupSizes)
        bsplit = []
        for i in range(n):
            bsplit.append([])
        print(bsplit)
        
        #split according to group size
        for i in range(n):
            v = groupSizes[i]-1
            bsplit[v].append(i)
        print(bsplit)
        
        ans = []
        for i in range(n):
            b = bsplit[i]
            k = len(b)
            if k == i+1:
                ans.append(b)
                continue
            for j in range(0,k-i,i+1):
                c = b[j:j+i+1]
                ans.append(c)
        print(ans)
        return ans
