# https://leetcode.com/problems/decode-xored-array/

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        new = []
        new.append(first)
        n = len(encoded)
        prev = copy.copy(first)
        for i in range(n):
            v = prev ^ encoded[i]
            new.append(v)
            prev = copy.copy(v)
        return new
