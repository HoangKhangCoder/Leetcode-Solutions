class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = -1
        for x in s:
            if x not in t[start + 1: ]:
                return False
            start = t[start + 1: ].index(x) + start + 1
            print(start)
            
        return True