class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid) - 1, len(grid[0]) - 1
        @cache
        def helper(r, c):
            if r == rows and c == cols:
                return grid[r][c]
            if r == rows:
                return grid[r][c] + helper(r, c + 1)
            if c == cols:
                return grid[r][c] + helper(r + 1, c)
            return grid[r][c] + min(helper(r, c + 1), helper(r + 1, c))
        return helper(0, 0)