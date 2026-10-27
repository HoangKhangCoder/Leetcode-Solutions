class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        board = ["#" * (n - 1) + "." if i > 0 else "." * n for i in range(m)]
        return board
