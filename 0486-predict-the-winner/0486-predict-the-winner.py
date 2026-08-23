class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # Idea: dp[i][j] = the maximum score difference the current player
        # can achieve over their opponent, when only the segment nums[i..j]
        # remains to be picked from. On each turn, the player can pick the
        # first element (i) or the last element (j) of the remaining
        # segment; after picking, the opponent plays optimally on what's
        # left, so the opponent's advantage is subtracted.
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        # Segment of length 1: the score difference is just that element's value
        for i in range(n):
            dp[i][i] = nums[i]

        # Iterate over increasing segment lengths so that shorter subproblems are already computed
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # Pick nums[i]: difference = nums[i] - (opponent's optimal difference on [i+1, j])
                # Pick nums[j]: difference = nums[j] - (opponent's optimal difference on [i, j-1])
                # The current player picks whichever option gives the larger difference
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

        # The first player wins or ties if the final difference is >= 0
        return dp[0][n - 1] >= 0