from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Sort the array ascending so the largest/smallest values are easy to access
        nums.sort()

        # The maximum product can come from one of two cases:
        # 1) The three largest numbers (all positive, or possibly negative but still yielding the largest product)
        # 2) The two smallest (most negative) numbers, whose product is a large positive number, times the largest number
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
