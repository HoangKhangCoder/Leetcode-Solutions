class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = sum(nums)
        repeatNum = s - sum(set(nums))
        return [repeatNum, n * (n + 1) // 2 - s + repeatNum]