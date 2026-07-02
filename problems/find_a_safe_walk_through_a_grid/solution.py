class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        gone = set()

        @cache
        def helper(health: int, r: int, c: int) -> bool:
            if health < 1:
                return False
                
            if r == rows - 1 and c == cols - 1:
                return True

            gone.add((r, c))

            for new_r, new_c in ((r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)):
                if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in gone:
                    next_health = health - 1 if grid[new_r][new_c] == 1 else health
                    
                    if helper(next_health, new_r, new_c):
                        return True

            gone.remove((r, c))
            return False

        start_health = health - 1 if grid[0][0] == 1 else health
        return helper(start_health, 0, 0)