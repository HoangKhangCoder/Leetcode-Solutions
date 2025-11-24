class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        val = 0
        ans = []
        for n in nums:
            val = (val * 2 + n) % 5
            ans.append(val == 0)
        return ans