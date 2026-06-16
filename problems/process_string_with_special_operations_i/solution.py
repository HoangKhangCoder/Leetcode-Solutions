class Solution:
    def processStr(self, s: str) -> str:
        res = ""
        for cha in s:
            if cha == "*":
                res = res[:-1]
            elif cha == "#":
                res *= 2
            elif cha == "%":
                res = res[::-1]
            else:
                res += cha
        return res