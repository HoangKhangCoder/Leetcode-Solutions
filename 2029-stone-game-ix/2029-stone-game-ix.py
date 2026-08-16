from collections import Counter
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnts = Counter(stone % 3 for stone in stones)
        if cnts[0] % 2 == 0:
            return min(cnts[1], cnts[2]) > 0
        return abs(cnts[1] - cnts[2]) > 2