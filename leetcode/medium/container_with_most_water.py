from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        low, high = 0, len(height) - 1

        while low != high:
            low_wall, high_wall = height[low], height[high]
            cur_area = min(low_wall, high_wall) * (high - low)

            if cur_area > max_area:
                max_area = cur_area

            if low_wall < high_wall:
                low += 1
            else:
                high -= 1

        return max_area
