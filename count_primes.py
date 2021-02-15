#https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        mm = 5*pow(10,6)+1
        sieve = [0]*(n+1)
        sieve[0] = 1
        sieve[1] = 1
        for i in range(2, n+1):
            j = i*2
            while j < n+1:
                sieve[j] = 1
                j += i
        count = 0
        for i in range(n):
            if sieve[i] == 0:
                count += 1
        return count
