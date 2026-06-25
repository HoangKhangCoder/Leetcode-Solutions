class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        subBoxes = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j])
                if (num <= 0) or (num > 9):
                    return False
                #row
                if num in rows[i]:
                    return False
                else:
                    rows[i].add(num)
                #column
                if num in columns[j]:
                    return False
                else:
                    columns[j].add(num)
                #box
                if num in subBoxes[(i//3)*3+j//3]:
                    return False
                else: 
                    subBoxes[(i//3)*3+j//3].add(num)
        return True