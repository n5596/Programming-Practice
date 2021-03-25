#https://leetcode.com/problems/queens-that-can-attack-the-king/

class Solution:
    def closest(self, q_list, king):
        idx = -1
        min_d = 100000
        for q in q_list:
            if abs(q[0]-king[0])+abs(q[1]-king[1]) < min_d:
                min_d = abs(q[0]-king[0])+abs(q[1]-king[1])
                idx = q
        return idx
    
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        row1 = []
        col1 = []
        row2 = []
        col2 = []
        diag1 = []
        diag2 = []
        diag3 = []
        diag4 = []
        
        for q in queens:
            if q[0] == king[0]: #same row
                if q[1] < king[1]:
                    row1.append(q)
                else:
                    row2.append(q)
            elif q[1] == king[1]: #same col
                if q[0] < king[0]:
                    col1.append(q)
                else:
                    col2.append(q)
            elif q[1]-king[1] == q[0]-king[0] and q[1]-king[1] >= 0 :
                diag1.append(q)
            elif king[1]-q[1] == king[0]-q[0]:
                diag2.append(q)
            elif q[1]-king[1] == (q[0]-king[0])*-1 and q[1]-king[1] >= 0 :
                diag3.append(q)
            elif king[1]-q[1] == (king[0]-q[0])*-1:
                diag4.append(q)
        
        #print(row1, row2, col1, col2, diag1, diag2,diag3,diag4)
        
        ans = []
        a1 = self.closest(row1, king)
        a2 = self.closest(row2, king)
        a3 = self.closest(col1, king)
        a4 = self.closest(col2, king)
        a5 = self.closest(diag1, king)
        a6 = self.closest(diag2, king)
        a7 = self.closest(diag3, king)
        a8 = self.closest(diag4, king)
        
        if a1 != -1:
            ans.append(a1)
        if a2 != -1:
            ans.append(a2)
        if a3 != -1:
            ans.append(a3)
        if a4 != -1:
            ans.append(a4)
        if a5 != -1:
            ans.append(a5)
        if a6 != -1:
            ans.append(a6)
        if a7 != -1:
            ans.append(a7)
        if a8 != -1:
            ans.append(a8)
        return ans
