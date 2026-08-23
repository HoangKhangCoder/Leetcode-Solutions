class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        # Try increasing n one at a time until we find a number whose digit
        # product is divisible by t. Since the problem constraints are small,
        # a sequential scan is fast enough.
        while True:
            product = 1
            remaining = n
            while remaining > 0:
                product *= remaining % 10
                remaining //= 10

            if product % t == 0:
                return n

            n += 1
