class Solution:
    def reverse(self, x: int) -> int:
        sign = (1, -1)[x < 0]
        x = abs(x)

        result = sign * int(str(x)[::-1])
        
        if -2**31 <= result <= 2**31 - 1:
            return result
        else:
            return 0
