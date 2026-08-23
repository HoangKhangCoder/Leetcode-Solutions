from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        xyArea = 0  # Area of the projection onto the XY plane (viewed from above)
        yzArea = 0  # Area of the projection onto the YZ plane (viewed from the left/right side)
        zxArea = 0  # Area of the projection onto the ZX plane (viewed from the front/back)

        for i in range(n):
            maxRow = 0  # Tallest height in row i (used for the YZ projection)
            maxCol = 0  # Tallest height in column i (used for the ZX projection)
            for j in range(n):
                # A cell with height > 0 contributes 1 unit of area to the XY projection
                if grid[i][j] > 0:
                    xyArea += 1

                # Update the tallest height seen so far in row i
                if grid[i][j] > maxRow:
                    maxRow = grid[i][j]

                # Update the tallest height seen so far in column i
                if grid[j][i] > maxCol:
                    maxCol = grid[j][i]

            yzArea += maxRow
            zxArea += maxCol

        # The sum of the three projected areas is the answer
        return xyArea + yzArea + zxArea
