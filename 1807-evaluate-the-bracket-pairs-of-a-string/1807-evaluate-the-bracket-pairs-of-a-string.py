class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        diction = {}
        for key, val in knowledge:
            diction[key] = val

        res = ""
        inBracket, bracket = "", False
        for char in s:
            if char == "(":
                bracket = True
            elif char == ")" and bracket == True:
                bracket = False
                if inBracket not in diction:
                    res += "?"
                else:
                    res += diction[inBracket]
                inBracket = ""
            elif bracket == True:
                inBracket += char
            else:
                res += char
        return res