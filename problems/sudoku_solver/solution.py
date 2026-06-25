class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        rowSet, colSet, cellSet = set(), set(), set()
        def placeNum(x, y, num):
            if (x, num) in rowSet or (y, num) in colSet or (x // 3, y // 3, num) in cellSet:
                return False
            return True

        openCells = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == ".":
                    openCells.append((i, j))
                else:
                    rowSet.add((i, board[i][j]))
                    colSet.add((j, board[i][j]))
                    cellSet.add((i // 3, j // 3, board[i][j]))
        
        def backtrack(idx):
            if idx >= len(openCells):
                return True
            r, c = openCells[idx]
            for num in "123456789":
                if placeNum(r, c, num):
                    rowSet.add((r, num))
                    colSet.add((c, num))
                    cellSet.add((r // 3, c // 3, num))
                    board[r][c] = num
                    if backtrack(idx + 1):
                        return True
                    rowSet.remove((r, num))
                    colSet.remove((c, num))
                    cellSet.remove((r // 3, c // 3, num))
                    board[r][c] = "."
            return False
        
        backtrack(0)