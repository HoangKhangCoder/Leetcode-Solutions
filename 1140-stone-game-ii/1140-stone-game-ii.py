from functools import cache
from itertools import accumulate
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        prefixSum = [0] + list(accumulate(piles))

        @cache
        def dp(i, m):
            if i + 2 * m >= n:
                return prefixSum[n] - prefixSum[i]
            res = 0
            for x in range(1, 2 * m + 1):
                res = max(res, prefixSum[n] - prefixSum[i] - dp(i + x, max(x, m)))
            return res
        return dp(0, 1)