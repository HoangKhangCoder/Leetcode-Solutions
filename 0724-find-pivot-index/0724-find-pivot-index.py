from itertools import accumulate
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        total = sum(nums)
        for i, num in enumerate(nums):
            rightSum = total - (leftSum + num)
            if rightSum == leftSum:
                return i
            leftSum += num
        return -1