class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        solutions = []

        def check(r, c, n):
            for x in board[r]:
                if x == "Q":
                    return False
            for row in range(n):
                if board[row][c] == "Q":
                    return False
            # up-right
            for move in range(n):
                row, col = r - move, c + move
                if row < 0 or col >= n:
                    break
                if board[row][col] == "Q":
                    return False
            # up-left
            for move in range(n):
                row, col = r - move, c - move
                if row < 0 or col < 0:
                    break
                if board[row][col] == "Q":
                    return False
            # down-right
            for move in range(n):
                row, col = r + move, c + move
                if row >= n or col >= n:
                    break
                if board[row][col] == "Q":
                    return False
            return True

        def backtracking(row):
            nonlocal n
            if row == n:
                res = []
                for row in board:
                    res.append("".join(row))
                solutions.append(res)
                return
            for col in range(n):
                if check(row, col, n):
                    board[row][col] = "Q"
                    backtracking(row + 1)
                    board[row][col] = "."
            return
        backtracking(0)
        return len(solutions)