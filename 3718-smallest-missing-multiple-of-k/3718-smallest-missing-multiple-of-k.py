class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        sets = set(nums)
        cur = k
        while True:
            if cur not in sets:
                return cur
            cur += k