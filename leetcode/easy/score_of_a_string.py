class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        last_score = ord(s[0])
        total = 0

        for i in range(1, n):
            cur_score = ord(s[i])
            total += abs(last_score - cur_score)
            last_score = cur_score

        return total