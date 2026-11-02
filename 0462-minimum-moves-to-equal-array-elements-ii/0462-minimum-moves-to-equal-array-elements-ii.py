class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid = nums[len(nums) // 2]
        return sum(abs(mid - x) for x in nums)