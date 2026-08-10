from math import isqrt
class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        dp = [False] * (n + 1)
        squares = [k ** 2 for k in range(1, isqrt(n) + 1)]
        for i in range(n + 1):
            if dp[i]:
                continue
            for sq in squares:
                if i + sq > n:
                    break
                dp[i + sq] = True
        return dp[n]