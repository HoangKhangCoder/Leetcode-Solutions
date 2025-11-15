class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def isNum(x: int):
            try:
                int(x)
                return True
            except:
                return False

        operators = ["+", "-", "*", "/"]
        def helper(tokens: List[int], n: int):
            if n == 1:
                return int(tokens[0])
            for i in range(n - 2):
                a = tokens[i]
                b = tokens[i + 1]
                o = tokens[i + 2]
                if isNum(a) and isNum(b) and o in operators:
                    return helper(tokens[:i] + [str(int(eval(a + o + b)))] + tokens[i + 3:], n - 2)
        return helper(tokens, len(tokens))