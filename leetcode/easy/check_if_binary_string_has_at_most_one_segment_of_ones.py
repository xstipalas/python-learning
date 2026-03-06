class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = int(s, 2)

        return bin(n & ~(n >> 1)).count('1') < 2