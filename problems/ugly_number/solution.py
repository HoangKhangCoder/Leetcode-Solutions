class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        def isPrime(x: int) -> bool:
            for i in range(2 + 1 * (x % 2), math.isqrt(x) + 1, 1 + x % 2):
                if x % i == 0:
                    return False
            return True

        for i in range(1, math.isqrt(n) + 1, 1 + n % 2):
            if n % i == 0:
                for q in [i, n // i]:
                    if isPrime(q) and q > 5:
                        return False
        return True