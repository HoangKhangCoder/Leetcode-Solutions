class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        preMax = [nums[0]] * n
        preMin = [nums[-1]] * n
        for i in range(1, n):
            preMax[i] = max(preMax[i - 1], nums[i])
            preMin[n - 1 - i] = min(preMin[n - i], nums[n - 1 - i])
        for i in range(n):
            if preMax[i] - preMin[i] <= k:
                return i
        return -1