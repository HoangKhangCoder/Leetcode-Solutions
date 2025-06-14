class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1 or len(nums) == len(set(nums)):
            return False

        index = 0
        while index < len(nums):
            check_nums = nums[index: index+k+1]
            check_len = k + 1
            if index + k + 1 >= len(nums):
                check_nums = nums[index:]
                check_len = len(check_nums)

            if len(set(check_nums)) < check_len:
                return True
            index+=1
        
        return False