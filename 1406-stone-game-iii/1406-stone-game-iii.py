from functools import cache
from typing import List


class Solution:
    def stoneGameIII(self, vals: List[int]) -> str:
        # dp(i) returns the best achievable score difference (current player's score - opponent's score)
        # when starting to take piles from index i onward
        @cache
        def dp(i=0):
            if i >= len(vals):
                return 0

            # Take 1 pile: the value gained minus the opponent's best result on the remainder
            best = vals[i] - dp(i + 1)

            # Take 2 consecutive piles (if enough remain)
            if i + 1 < len(vals):
                best = max(best, sum(vals[i: i + 2]) - dp(i + 2))

            # Take 3 consecutive piles (if enough remain)
            if i + 2 < len(vals):
                best = max(best, sum(vals[i: i + 3]) - dp(i + 3))

            return best

        diff = dp()
        if diff > 0:
            return 'Alice'
        elif diff < 0:
            return 'Bob'
        return 'Tie'
