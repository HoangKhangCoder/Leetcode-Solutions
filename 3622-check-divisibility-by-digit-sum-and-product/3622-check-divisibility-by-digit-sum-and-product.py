class Solution:
    def checkDivisibility(self, n: int) -> bool:
        prod = 1
        s = 0
        for d in str(n):
            s += int(d)
            prod *= int(d)
        return n % (s + prod) == 0