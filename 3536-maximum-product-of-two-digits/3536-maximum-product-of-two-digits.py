class Solution:
    def maxProduct(self, n: int) -> int:
        # Convert n into its digits, sort them in ascending order, then take
        # the two largest digits (the last two elements after sorting) so
        # their product is maximized.
        digit1, digit2 = sorted(str(n))[-2:]
        return int(digit1) * int(digit2)
