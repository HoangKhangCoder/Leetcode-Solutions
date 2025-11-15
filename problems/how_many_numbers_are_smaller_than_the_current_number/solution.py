class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sorted = sorted(nums)
        value_to_count = {}
        for i in range(len(nums_sorted)):
            current_value = nums_sorted[i]
            if current_value not in value_to_count:
                value_to_count[current_value] = i
        result = []
        for num in nums:
            result.append(value_to_count[num])
        return result