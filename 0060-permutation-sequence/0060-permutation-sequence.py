import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n + 1)]
        k -= 1
        
        res = 0
        fact = math.factorial(n - 1)
        
        for i in range(n - 1, 0, -1):
            idx = k // fact
            res = res * 10 + nums.pop(idx)
            k %= fact
            fact //= i
        
        res = res * 10 + nums[0]
        return str(res)