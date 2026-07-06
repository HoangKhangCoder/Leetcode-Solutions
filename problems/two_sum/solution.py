class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cnt = Counter(nums)
        for i, x in enumerate(nums):
            y = target - x
            if y in cnt and (y != x or cnt[y] > 1):
                return [i, nums[i + 1: ].index(y) + i + 1]