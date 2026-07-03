class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse=True)
        selected = nums[:k]
        
        total_sum = 0
        current_mul = mul
        
        for x in selected:
            total_sum += max(x, x * current_mul)
            current_mul -= 1
            
        return total_sum