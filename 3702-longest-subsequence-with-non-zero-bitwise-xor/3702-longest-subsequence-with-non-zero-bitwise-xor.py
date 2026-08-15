class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0
        allZeros = True
        for num in nums:
            if num != 0:
                allZeros = False
                xor ^= num
        if allZeros:
            return 0
        if xor == 0:
            return len(nums) - 1
        return len(nums)