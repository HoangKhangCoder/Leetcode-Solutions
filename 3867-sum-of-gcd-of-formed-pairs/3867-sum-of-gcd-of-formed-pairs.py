from math import gcd


class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGcd = [0] * n

        # For each position i, compute the GCD between nums[i] and the
        # maximum value seen from the start of the array up to position i
        # (currentMax). This builds the prefixGcd array used for pairing in
        # the next step.
        currentMax = nums[0]
        for i in range(n):
            if nums[i] > currentMax:
                currentMax = nums[i]
            prefixGcd[i] = gcd(nums[i], currentMax)

        # Sort the prefixGcd array so we can pair the largest with the
        # smallest (two-pointer technique) in order to optimize the total
        # GCD sum as required by the problem.
        prefixGcd.sort()

        totalSum = 0
        left = 0
        right = n - 1

        # Pair the smallest remaining element with the largest remaining
        # element, accumulating the GCD of each pair into the total result.
        while left < right:
            totalSum += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return totalSum
