from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Since the number of piles is always even, the first player (Alex) always has
        # a strategy that guarantees a win (for example, always taking every pile at an
        # even index, or every pile at an odd index, whichever group has the larger sum)
        # Therefore the result is always True
        return True
