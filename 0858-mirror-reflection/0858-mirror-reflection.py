class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        com = math.gcd(p, q)
        p //= com
        q //= com
        
        if p % 2 == 0:
            return 2
        elif q % 2 == 0:
            return 0
        else:
            return 1