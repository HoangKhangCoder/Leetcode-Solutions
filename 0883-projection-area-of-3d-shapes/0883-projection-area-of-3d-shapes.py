class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        xy_area = 0
        yz_area = 0
        zx_area = 0
        
        for i in range(n):
            max_row = 0
            max_col = 0
            for j in range(n):
                if grid[i][j] > 0:
                    xy_area += 1
                
                if grid[i][j] > max_row:
                    max_row = grid[i][j]
                
                if grid[j][i] > max_col:
                    max_col = grid[j][i]
                    
            yz_area += max_row
            zx_area += max_col
            
        return xy_area + yz_area + zx_area