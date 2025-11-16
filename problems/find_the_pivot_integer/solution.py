class Solution:
    def pivotInteger(self, n: int) -> int:
        s = n * (n + 1) // 2
        res = math.isqrt(s)
        if res ** 2 == s:
            return res
        return -1