class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        return ["#" * (n - 1) + "." if i > 0 else "." * n for i in range(m)]