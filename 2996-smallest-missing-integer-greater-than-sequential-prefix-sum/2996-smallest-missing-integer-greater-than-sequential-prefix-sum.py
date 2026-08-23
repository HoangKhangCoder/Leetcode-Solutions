class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Step 1: Find the sum of the leading "sequential prefix", i.e. the
        # initial run of the array where each element is exactly 1 greater
        # than the element before it.
        numSet = set(nums)
        result = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] != 1:
                break
            result += nums[i]

        # Step 2: Keep incrementing result until we find a value not present in the array
        while result in numSet:
            result += 1

        return result
