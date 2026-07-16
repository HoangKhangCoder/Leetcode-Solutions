from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGcd = [0] * n

        current_max = nums[0]
        for i in range(n):
            if nums[i] > current_max:
                current_max = nums[i]
            prefixGcd[i] = gcd(nums[i], current_max)

        prefixGcd.sort()

        total_sum = 0
        left = 0
        right = n - 1

        while left < right:
            total_sum += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return total_sum