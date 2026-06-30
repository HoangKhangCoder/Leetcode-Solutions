class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        lastPos = [-1] * 3
        cnt = n
        base = ord("a")
        for i in range(len(s)):
            char = s[i]
            lastPos[ord(char) - base] = i
            cnt += min(lastPos)
        return cnt