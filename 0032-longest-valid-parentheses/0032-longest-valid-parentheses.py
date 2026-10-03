class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        pen = -1
        for i, char in enumerate(s):
            if char == ")":
                if len(stack) == 1:
                    pen = i
                    continue
                stack.pop()
                res = max(res, i - max(stack[-1], pen))
                continue
            stack.append(i)
        return res