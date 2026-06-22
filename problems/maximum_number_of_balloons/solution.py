class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        seen = Counter(text)
        res = seen['b']
        for char in ('a', 'l', 'o', 'n'):
            num = seen[char]
            if char in ('l', 'o'):
                res = min(res, seen[char] // 2)
                continue
            res = min(res, num)
        return res