class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return all(self.isPalindromic(self.convert_to(n, base)) for base in range(2, n - 1))
    
    @staticmethod
    def convert_to(n: int, base: int) -> str:
        abc = '0123456789ABCDEF'
        result = []

        while n > 0:
            result.append(abc[n % base])

            n //= base

        return ''.join(result)

    @staticmethod
    def isPalindromic(line: str) -> bool:
        mid = len(line) // 2

        return line[:mid] == line[-1:mid:-1]