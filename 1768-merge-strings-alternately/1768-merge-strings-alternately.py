class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        i = 0
        res = ""
        while i < min(n, m):
            res += word1[i] 
            res += word2[i]
            i += 1
        if i < n:
            res += word1[i:]
        if i < m:
            res += word2[i:]
        return res