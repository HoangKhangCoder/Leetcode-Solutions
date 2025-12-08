class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for a in range(1, n + 1):
            for b in range(a, n + 1):
                s = b ** 2 + a ** 2
                c = math.sqrt(s)
                if c <= n and c == math.isqrt(s):
                    cnt += 1
                    if b != a:
                        cnt += 1
        return cnt