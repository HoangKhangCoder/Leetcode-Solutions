class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # Put the existing elements into a set for O(1) membership lookups.
        numSet = set(nums)

        # Iterate over every value in the range [min(nums), max(nums)] and
        # collect those values that do not appear in nums.
        return [value for value in range(min(nums), max(nums) + 1) if value not in numSet]
