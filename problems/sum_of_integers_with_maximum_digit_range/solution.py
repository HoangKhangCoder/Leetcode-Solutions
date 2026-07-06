class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        range = []
        _nums = {}
        
        for num in nums:
            digits = list(map(int, list(str(num))))
            res = max(digits) - min(digits)
            _nums[num] = res
            range.append(res)
            
        maxRange = max(range)
        s = 0
        for num in nums:
            if _nums[num] == maxRange:
                s += num
        return s