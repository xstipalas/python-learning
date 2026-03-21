class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        nums_count = {}
        result = 0

        for num in nums:
            if num in nums_count:
                result += nums_count[num]
                nums_count[num] += 1
            else:
                nums_count[num] = 1

        return result
