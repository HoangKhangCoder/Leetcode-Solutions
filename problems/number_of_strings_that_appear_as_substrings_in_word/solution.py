class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        cnt = 0
        for s in patterns:
            cnt += int(s in word)
        return cnt