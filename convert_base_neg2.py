#https://leetcode.com/problems/convert-to-base-2/

class Solution:
    def baseNeg2(self, N: int) -> str:
        s = ''
        temp = N
        if N == 0:
            return "0"
        
        while abs(temp) >= 1:
            digit = int(fmod(temp, -2))
            temp /= -2
            if digit < 0:
                temp += 1
                digit = digit + 2
            s = s + str(digit)

        return  s[::-1]
