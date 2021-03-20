#https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = []
        ind = [0]*n
        for e in edges:
            v2 = e[1]
            ind[v2] += 1
        for i in range(len(ind)):
            if ind[i] == 0:
                ans.append(i)
        return ans
