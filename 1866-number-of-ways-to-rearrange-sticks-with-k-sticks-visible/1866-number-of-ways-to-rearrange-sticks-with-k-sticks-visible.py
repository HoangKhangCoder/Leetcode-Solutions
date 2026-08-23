class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        # Dynamic programming: dp[i][j] = number of ways to arrange i sticks
        # so that exactly j of the tallest-so-far sticks are visible from one side.
        #
        # Consider where stick i (the "new" stick compared to the i-1 sticks
        # problem) is placed:
        #   - If stick i is placed as the TALLEST stick (leading the sequence
        #     as seen by the viewer), it is guaranteed to be visible -> there
        #     are dp[i-1][j-1] ways to arrange the remaining (i-1) sticks so
        #     that j-1 of them are visible.
        #   - If stick i is placed in one of the other (i-1) positions (not the
        #     tallest position), it will be blocked from view by a taller stick
        #     ahead of it (it does not add to the visible count) -> there are
        #     (i-1) ways to choose its position, multiplied by dp[i-1][j] ways
        #     to arrange the rest.
        # Hence: dp[i][j] = dp[i-1][j-1] + (i-1) * dp[i-1][j]
        # Base case: when i == j (every stick must be visible), there is
        # exactly 1 valid arrangement — each stick taller than the one before
        # it (dp[i][j] = 1).
        MOD = 10 ** 9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[1][1] = 1

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                if i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = ((i - 1) * dp[i - 1][j] + dp[i - 1][j - 1]) % MOD

        return dp[n][k] % MOD
