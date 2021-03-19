#https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/submissions/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0]*n
        ones = []
        
        #all indices with a ball
        for b in range(n):
            if boxes[b] == '1':
                ones.append(b)
        
        for i in range(n):
            count = 0
            for j in ones:
                count += abs(i-j)
            #print('count', count)
            ans[i] = count
            
        return ans
        
