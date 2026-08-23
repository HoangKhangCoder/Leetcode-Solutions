class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xorAll = 0
        allZeros = True

        # Compute the XOR of the whole array (zeros are skipped since XOR-ing
        # with 0 doesn't change the value, but we still need to know whether
        # the array consists entirely of zeros).
        for num in nums:
            if num != 0:
                allZeros = False
                xorAll ^= num

        # If every element is 0, then every subsequence's XOR is 0,
        # so no subsequence can have a non-zero XOR.
        if allZeros:
            return 0

        # If the XOR of the whole array is 0, we can drop any single non-zero
        # element so the remainder has a non-zero XOR, giving a maximum length of n - 1.
        if xorAll == 0:
            return len(nums) - 1

        # If the XOR of the whole array is already non-zero, taking the entire array is optimal.
        return len(nums)
