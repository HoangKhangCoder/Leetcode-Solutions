class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        setNums = set(nums)
        while original in setNums:
            original *= 2
        return original