class Solution:
    def lastRemaining(self, n: int) -> int:
        def helper(n: int, direct: int, head: int, steps: int) -> int:
            if n == 1:
                return head
            if direct or n % 2:
                head += steps
            return helper(n // 2, (direct - 1) % 2, head, steps * 2)
        return helper(n, 1, 1, 1)