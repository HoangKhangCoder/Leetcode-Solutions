class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l = r = 0
        res = k
        cnts = {}
        while r < len(nums):
            num = nums[r]
            cnts[num] = cnts.get(num, 0) + 1
            while cnts[num] > k:
                cnts[nums[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
            r += 1
        return res