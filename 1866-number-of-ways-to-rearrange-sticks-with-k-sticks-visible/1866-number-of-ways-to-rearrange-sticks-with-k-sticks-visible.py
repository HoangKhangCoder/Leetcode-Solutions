class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        # dp[n][k] = (n - 1) * dp[n - 1][k] + dp[n - 1][k - 1] if n ≠ k else 1
        MOD = 10 ** 9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[1][1] = 1
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                if i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = (i - 1) * dp[i - 1][j] + dp[i - 1][j - 1]

        return (dp[n][k]) % MOD