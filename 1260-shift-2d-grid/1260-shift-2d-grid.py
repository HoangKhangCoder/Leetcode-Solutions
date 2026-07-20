from copy import deepcopy
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        setup = [[0] * n for _ in range(m)]
        for _ in range(k):
            new = deepcopy(setup)
            for i in range(m):
                for j in range(n):
                        if i == m - 1 and j == n - 1:
                            new[0][0] = grid[i][j]
                        elif j == n - 1:
                            new[i + 1][0] = grid[i][j]
                        else:
                            new[i][j + 1] = grid[i][j]
            grid = deepcopy(new)
        return grid