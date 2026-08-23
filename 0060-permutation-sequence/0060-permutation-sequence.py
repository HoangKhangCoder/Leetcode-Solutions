import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Idea: with n numbers {1..n}, there are n! permutations arranged in
        # lexicographic order. Once we fix the first digit, there are (n-1)!
        # permutations of the remaining digits. We divide (k-1) by (n-1)! to
        # find the index of the first digit to pick, then shrink the problem
        # and repeat.
        nums = [i for i in range(1, n + 1)]
        k -= 1  # switch to a 0-based index to simplify the arithmetic

        res = 0
        fact = math.factorial(n - 1)  # number of permutations for each choice of the first digit

        for i in range(n - 1, 0, -1):
            idx = k // fact          # index of the number to take from the remaining list
            res = res * 10 + nums.pop(idx)  # append this digit to the result and remove it from the list
            k %= fact                # the remainder determines the position within the sub-group of permutations
            fact //= i                # update the factorial for the next step (one fewer element remains)

        # Only one number is left in nums, and it's the last digit
        res = res * 10 + nums[0]
        return str(res)