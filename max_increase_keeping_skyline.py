#https://leetcode.com/problems/max-increase-to-keep-city-skyline/submissions/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        vertical = [] #top/bottom
        horizontal = [] #left/right
        
        #row
        for i in range(n):
            row = grid[i]
            horizontal.append(max(row))
            
        #col
        for j in range(m):
            col = [sub[j] for sub in grid] 
            vertical.append(max(col))
        
        print(horizontal)
        print(vertical)
        
        inc = 0
        for i in range(n):
            for j in range(m):
                inc += max(abs(grid[i][j]-min(vertical[j],horizontal[i])),0)
        return inc
