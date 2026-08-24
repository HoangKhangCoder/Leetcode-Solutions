from itertools import accumulate
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        prefixSum = list(accumulate(stones))
        dp = prefixSum[-1]
        for i in range(len(stones) - 2, 0, -1):
            dp = max(dp, prefixSum[i] - dp)
        return dp