from copy import deepcopy
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        template = [[0] * n for _ in range(m)]

        # Shift the grid one step at a time, repeated k times
        for _ in range(k):
            newGrid = deepcopy(template)
            for i in range(m):
                for j in range(n):
                    if i == m - 1 and j == n - 1:
                        # The element at the bottom-right corner wraps around to the first position
                        newGrid[0][0] = grid[i][j]
                    elif j == n - 1:
                        # The last element of a row moves to the start of the next row
                        newGrid[i + 1][0] = grid[i][j]
                    else:
                        # All other elements shift one cell to the right
                        newGrid[i][j + 1] = grid[i][j]
            grid = deepcopy(newGrid)

        return grid
