class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n = len(s)
        stack = []
        res = ''
        for num in s:
            if num == '(':
                if stack:
                    res += num
                stack.append(num)
                continue
            stack.pop()
            if stack:
                res += num
                
        return res
