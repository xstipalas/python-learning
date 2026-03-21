class Solution:
    def reverseDegree(self, s: str) -> int:
        REVERSE_OFFSET = ord('a') + 26

        return sum(i * (-ord(ch) + REVERSE_OFFSET) for i, ch in enumerate(s, 1))