import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]
        k -= 1
        
        result = []
        fact = math.factorial(n - 1)
        
        for i in range(n - 1, 0, -1):
            idx = k // fact
            result.append(nums.pop(idx))
            k %= fact
            fact //= i
        
        result.append(nums[0])
        return "".join(result)