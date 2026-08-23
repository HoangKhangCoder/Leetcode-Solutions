import math


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # Reduce the ratio p:q to lowest terms using the greatest common divisor (gcd),
        # since the problem's outcome only depends on the parity of p and q after reduction
        gcdVal = math.gcd(p, q)
        p //= gcdVal
        q //= gcdVal

        # After reduction, p and q cannot both be even
        # - If p is even: the light ray hits the top-right corner first -> receptor (2)
        # - If q is even: the light ray hits the bottom-right corner first -> receptor (0)
        # - If both are odd: the light ray hits the top-left corner -> receptor (1)
        if p % 2 == 0:
            return 2
        elif q % 2 == 0:
            return 0
        else:
            return 1
