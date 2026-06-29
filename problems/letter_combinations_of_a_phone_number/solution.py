class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        chars = {}
        base = ord("a")
        for num in [i for i in range(2, 7)]:
            chars[num] = [chr(base + (num - 2) * 3 + i) for i in range(3)]

        chars[7] = ["p", "q", "r", "s"]
        chars[8] = ["t", "u", "v"]
        chars[9] = ["w", "x", "y", "z"]

        def helper(left, cur):
            if not left:
                res.append(cur)
                return
            num = int(left[0])
            left = left[1:]
            for char in chars[num]:
                helper(left, cur + char)
        helper(digits, "")
        return res