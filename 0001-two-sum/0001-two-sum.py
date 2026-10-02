class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        cnt = Counter(nums)
        sets = set(nums)
        for x in nums:
            y = target - x
            if y in sets and (cnt[x] >= 2 or x != y):
                return [nums.index(x), nums[nums.index(x) + 1:].index(y) + nums.index(x) + 1]
        