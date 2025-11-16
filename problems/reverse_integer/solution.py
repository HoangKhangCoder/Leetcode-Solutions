class Solution:
    def reverse(self, x: int) -> int:
        revNum = int("-" * (x < 0) + str(abs(x))[::-1])
        if revNum < -2**31 or revNum > 2 ** 31 - 1:
            return 0
        return revNum