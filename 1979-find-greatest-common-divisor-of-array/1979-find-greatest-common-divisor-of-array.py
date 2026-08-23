from math import gcd


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # The greatest common divisor (GCD) of the whole array equals the GCD
        # of its smallest and largest elements, since the GCD of the full set
        # of numbers can never exceed the GCD of the (min, max) pair, and any
        # divisor of both min and max also divides every value between them.
        return gcd(max(nums), min(nums))
