class Solution:
    def tribonacci(self, n: int) -> int:
        nums = [0, 1, 1]
        while len(nums) <= n:
            nums.append(nums[-1] + nums[-2] + nums[-3])
        return nums[n]