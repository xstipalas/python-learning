from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        cache = {num: bin(num).count('1') for num in arr}

        return list(sorted(arr, key=lambda x: (cache[x], x)))
