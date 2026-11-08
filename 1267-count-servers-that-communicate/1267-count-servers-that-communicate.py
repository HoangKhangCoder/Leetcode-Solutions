class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rowsValid = [max(grid[i].count(1) - 1, 0) for i in range(len(grid))]
        colsValid = []
        for col in range(len(grid[1])):
            cur = -1
            for row in range(len(grid)):
                if grid[row][col] == 1:
                    cur += 1
                if cur == 1:
                    break
            colsValid.append(cur)

        cnt = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (rowsValid[row] or colsValid[col]):
                    cnt += 1
        return cnt