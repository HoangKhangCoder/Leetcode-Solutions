class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        s = 0
        for digit in str(n):
            digit = int(digit)
            if digit:
                x = x * 10 + digit
                s += digit
        return x * s