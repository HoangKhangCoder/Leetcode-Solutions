from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnts = Counter(s)
        sortedS = sorted(set(s))
        res = ""
        mid = ""
        for char in sortedS:
            cnt = cnts[char]
            mid += char * (cnt % 2)
            res += char * (cnt // 2)
        return res + mid + res[::-1]