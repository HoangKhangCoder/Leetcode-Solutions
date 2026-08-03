from functools import cache
class Solution:
    def stoneGameIII(self, vals: List[int]) -> str:
        @cache
        def dp(i=0):
            if i >= len(vals):
                return 0
            cur = vals[i] - dp(i + 1)
            if i + 1 < len(vals):
                cur = max(cur, sum(vals[i: i + 2]) - dp(i + 2))
            if i + 2 < len(vals):
                cur = max(cur, sum(vals[i: i + 3]) - dp(i + 3))
            return cur
        res = dp()
        if res > 0:
            return 'Alice'
        elif res < 0:
            return 'Bob'
        return 'Tie'