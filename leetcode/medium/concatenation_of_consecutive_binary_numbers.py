class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        result = 1

        for num in range(2, n + 1):
            result = ((result << (num.bit_length() or 1)) | num) % (MOD)

        return result
