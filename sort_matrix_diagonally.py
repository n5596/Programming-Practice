#https://leetcode.com/problems/sort-the-matrix-diagonally/

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        
        #vertical diag
        for i in range(n-2,-1,-1):
            diag = []
            for j in range(m):
                if i+j >= n or j >= m:
                    break
                diag.append(mat[i+j][j])
            diag.sort()
            for j in range(len(diag)): #i+1
                mat[i+j][j] = diag[j]
                
        #horizontal diag
        for i in range(1,m):
            diag = []
            for j in range(n):
                if i+j >= m or j >= n:
                    break
                diag.append(mat[j][i+j])
            diag.sort()
            for j in range(len(diag)):
                mat[j][i+j] = diag[j]
            
        return mat
