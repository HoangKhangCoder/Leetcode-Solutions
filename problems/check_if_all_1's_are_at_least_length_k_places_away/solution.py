class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prevNum = -float("inf")
        for i, x in enumerate(nums):
            if x == 1:
                if i - prevNum - 1 < k:
                    return False
                prevNum = i
        return True