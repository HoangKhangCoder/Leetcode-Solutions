from functools import cache
from itertools import accumulate
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        # Prefix sum array: prefixSum[i] = sum of elements from index 0..i-1
        prefixSum = [0] + list(accumulate(piles))

        # dp(i, m) returns the maximum number of stones the CURRENT player can take
        # starting from pile i, where the allowed move size X is in the range [1, 2*m]
        @cache
        def dp(i, m):
            # If the remaining piles number <= 2*m, the current player can take all of them
            if i + 2 * m >= n:
                return prefixSum[n] - prefixSum[i]

            best = 0
            # Try every possible choice of X from 1 to 2*m piles
            for x in range(1, 2 * m + 1):
                # Stones taken now = remaining total - the opponent's best result afterward
                best = max(best, prefixSum[n] - prefixSum[i] - dp(i + x, max(x, m)))
            return best

        return dp(0, 1)
