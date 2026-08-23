from math import log


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)

        # For n <= 2, the maximum number of distinct values that can be
        # produced by XOR-ing triplets (indices are allowed to repeat) is
        # exactly n (a special case stated by the problem).
        if n <= 2:
            return n

        # For n >= 3, since nums[i] lies in the range [1, n], the number of
        # bits needed to represent it is floor(log2(n)) + 1. Once we have 3
        # or more elements available, the XOR of any 3 numbers (indices may
        # repeat) can produce every value in [0, 2^bit - 1], so the answer
        # is 2^bit.
        bitLength = int(log(n, 2)) + 1
        return pow(2, bitLength)
