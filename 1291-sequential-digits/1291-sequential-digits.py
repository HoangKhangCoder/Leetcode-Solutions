class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        ways = []
        for i in range(9):
            for j in range(i, 9):
                num = int(digits[i: j + 1])
                if num < low or num > high:
                    continue
                ways.append(num)
        ways.sort()
        return ways