class Solution:
    def climbStairs(self, n: int) -> int:
        # Idea: this is a Fibonacci-sequence problem. To reach step n, you
        # can either come from step (n-1) with a 1-step move, or from step
        # (n-2) with a 2-step move. So the number of ways = ways to reach
        # (n-1) + ways to reach (n-2).
        if n <= 2:
            return n
        a, b = 1, 1  # a: number of ways to reach step (i-1), b: ways to reach step i
        for i in range(n - 1):
            a, b = b, a + b  # slide the Fibonacci window forward
        return b