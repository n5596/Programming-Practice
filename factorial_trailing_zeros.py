#https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        count2 = 0
        count5 = 0
        for i in range(1, n+1):
            while i % 2 == 0:
                i /= 2
                count2 += 1
            while i % 5 == 0:
                i /= 5
                count5 += 1
        return min(count2, count5)
