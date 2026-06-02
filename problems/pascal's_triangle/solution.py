class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1] for _ in range(numRows)]
        for rowIdx in range(2, numRows + 1):
            row = [1] * rowIdx
            for i in range(1, rowIdx - 1):
                row[i] = triangle[rowIdx-2][i - 1] + triangle[rowIdx-2][i]
            triangle[rowIdx - 1] = row
        return triangle