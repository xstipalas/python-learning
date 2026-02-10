class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            return self.rle(self.countAndSay(n - 1))

    @staticmethod
    def rle(string_: str) -> str:
        result = ''
        last = string_[0]
        count = 0

        for ch in string_:
            if ch == last:
                count += 1
            else:
                result += str(count) + last

                last = ch
                count = 1

        result += str(count) + last

        return result
