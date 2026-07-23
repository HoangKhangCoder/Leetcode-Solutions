from math import log
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        return pow(2, int(log(len(nums), 2)) + 1)