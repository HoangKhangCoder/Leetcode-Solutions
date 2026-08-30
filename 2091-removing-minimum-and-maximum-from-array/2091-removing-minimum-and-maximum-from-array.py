class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        maxIdx = nums.index(max(nums)) + 1
        minIdx = nums.index(min(nums)) + 1
        return min(maxIdx + (n - minIdx + 1), max(maxIdx, minIdx), n - min(maxIdx, minIdx) + 1, minIdx + (n - maxIdx + 1))