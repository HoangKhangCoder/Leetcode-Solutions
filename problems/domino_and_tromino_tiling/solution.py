class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n
        if n == 3:
            return 5
        dp = [0] * (n + 1)
        dp[1: 4] = [1, 2, 5]
        MOD = 10 ** 9 + 7
        for i in range(4, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD
        return dp[-1]