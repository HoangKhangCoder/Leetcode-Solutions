class Solution:
    def maxRepeating(self, s: str, pattern: str) -> int:
        k = 1
        while pattern * k in s:
            k += 1
        return k - 1