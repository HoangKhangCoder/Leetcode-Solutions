from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # leftSum: sum of all elements to the left of the current index
        # total: sum of the entire array
        leftSum = 0
        total = sum(nums)

        for i, num in enumerate(nums):
            # rightSum = total sum - (left sum + current element)
            rightSum = total - (leftSum + num)
            if rightSum == leftSum:
                return i
            # Update the left sum after processing the current element
            leftSum += num

        # No pivot index found
        return -1
