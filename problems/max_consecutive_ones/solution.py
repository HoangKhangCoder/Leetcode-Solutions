class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCon = 0
        con = 0
        for cha in nums:
            if cha == 1:
                con += 1
            else:
                maxCon = max(maxCon, con)
                con = 0
        maxCon = max(maxCon, con)
        return maxCon