from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Sort ascending; the two largest elements end up at the end of the array
        nums.sort()
        # Result = (largest element - 1) * (second largest element - 1)
        return (nums[-1] - 1) * (nums[-2] - 1)
