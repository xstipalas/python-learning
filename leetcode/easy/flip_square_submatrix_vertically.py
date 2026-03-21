class Solution:
    def reverseSubmatrix(self, grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        for i in range(k // 2):
            top = i + x
            bottom = x + k - i - 1

            grid[top][y:y+k], grid[bottom][y:y+k] = grid[bottom][y:y+k], grid[top][y:y+k]

        return grid