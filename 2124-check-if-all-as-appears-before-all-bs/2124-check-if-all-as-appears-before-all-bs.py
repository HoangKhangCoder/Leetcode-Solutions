class Solution:
    def checkString(self, s: str) -> bool:
        kinds = set(s)
        if len(kinds) > 2:
            return False
        return s.rfind("a") < s.find("b") or s.find("b") == -1