#https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, s: str) -> str:
        di = {}
        for i in s:
            if i in di:
                di[i] += 1
            else:
                di[i] = 1
        sort = sorted(di.values())
        print(sort, di.keys())
        
        vis = []
        n = ''
        for i in sort:
            for j in di.keys():
                if di[j] == i and j not in vis:
                    n = n+j*i
                    vis.append(j)
                    break
        return n[::-1]
