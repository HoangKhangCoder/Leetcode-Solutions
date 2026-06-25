class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        solutions = []

        def is_safe(row, col):

            # Check column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
                
            # Check the top of the left to the bottom of the right
            r, c = row, col
            while r >= 0 and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1

            # Check the top of the right to the bottom of the left
            r, c = row, col
            while r >= 0 and c < n:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c += 1

            return True
        
        def backtracking(row):
            if n == row:
                current_solution = ["".join(r) for r in board]
                solutions.append(current_solution)
                return
            
            for col in range(n):
                if is_safe(row, col):
                    # Mark Queen
                    board[row][col] = "Q"

                    # Continue backtracking
                    backtracking(row + 1)

                    # Test another way
                    board[row][col] = '.'
        
        backtracking(0)
        return solutions