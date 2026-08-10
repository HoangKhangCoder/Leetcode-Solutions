class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        dp = [False] * (n + 1)
        for i in range(n + 1):
            if dp[i]:
                continue
            k = 1
            while i + k ** 2 <= n:
                dp[i + k ** 2] = True
                k += 1
        return dp[n]