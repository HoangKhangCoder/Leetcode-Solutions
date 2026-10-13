class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(key=lambda x: abs(x))
        score = 0
        for i in range(n):
            if i % 2 == 0:
                score += nums[n - (i // 2) - 1] ** 2
            else:
                score -= nums[i // 2] ** 2
        return score