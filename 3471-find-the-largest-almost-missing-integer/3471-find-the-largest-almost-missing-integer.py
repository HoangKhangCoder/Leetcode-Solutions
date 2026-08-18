class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        cnts = {}
        for i in range(len(nums) - k + 1):
            for num in list(set(nums[i: i + k])):
                cnts[num] = cnts.get(num, 0) + 1
        res = -1
        for pair in cnts.items():
            if pair[1] > 1:
                continue
            res = max(res, pair[0])
        return res