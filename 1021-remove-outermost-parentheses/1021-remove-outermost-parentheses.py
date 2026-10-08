class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        bracket = 0
        for c in s:
            if c == "(":
                bracket += 1
                if bracket == 1: continue
            if c == ")":
                bracket -= 1
                if bracket == 0: continue
            ans += c
        return ans