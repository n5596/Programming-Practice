#https://leetcode.com/problems/minimum-operations-to-make-array-equal/

class Solution:
    def minOperations(self, n: int) -> int:
        count = n*n #sum of n numbers in series 1,3,5,... is n*n
        div = count/n #we need to have count/n = n at each index
        sums = 0
        if n%2 == 0:
            for i in range(int(n/2)):
                sums += (2*i)+1
        else:
            for i in range(int((n-1)/2)):
                sums += (2*i)+2
        return sums
        
