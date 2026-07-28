class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 1
        for i in range(n - 1):
            print(b)
            a, b = b, a + b
        return b