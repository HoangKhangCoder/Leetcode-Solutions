class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            val = nums[mid]
            print(l, r, mid, val)
            if val == target:
                return mid
            if val < target:
                l = mid + 1
            else:
                r = mid
        
        return l