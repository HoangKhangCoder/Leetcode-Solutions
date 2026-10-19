class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        ans = []
        for i, x in enumerate(nums):
            if x == target: ans.append(i)
        return ans