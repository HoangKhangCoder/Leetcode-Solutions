import numpy as np
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        return  int(min(
            (p:= np.partition(nums, [0,1,2, (n:=len(nums))-3, n-2, n-1]))[n-2] -p[1],
            p[n-3] -p[0],
            p[n-1] -p[2]
        ))
        