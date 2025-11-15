class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        def discount(x: int, i: int):
            for y in prices[i + 1:]:
                if y <= x:
                    return x - y
            return x
        ans = []
        for i, x in enumerate(prices):
            ans.append(discount(x, i))
        return ans