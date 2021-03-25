#https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        n = 250
        fib = [0]*n
        fib[1] = 1
        fib[2] = 1
        for i in range(3,n):
            fib[i] = fib[i-1]+fib[i-2]
        
        s = k
        j = n-1
        count = 1
        flag = 0
        
        while s > 0:
            if s-fib[j] >= 0:
                flag = 1
                s -= fib[j]
                if s == 0:
                    break
            else:
                j -= 1
                if flag == 1:
                    count += 1
                flag = 0
                
        return count
