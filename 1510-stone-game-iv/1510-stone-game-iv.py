from functools import cache
class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        @cache
        def dp(rem):
            if rem == 0:
                return False
            k = 1
            while k ** 2 <= rem:
                if not dp(rem - k ** 2):
                    return True
                k += 1
            return False
        return dp(n)