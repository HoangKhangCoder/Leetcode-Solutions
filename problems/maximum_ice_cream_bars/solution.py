class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cnt = 0
        for x in costs:
            if x > coins:
                return cnt
            coins -= x
            cnt += 1
        return cnt