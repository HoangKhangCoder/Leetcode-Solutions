from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        cnts = list(Counter(word).items())
        cnts.sort(key=lambda pair: pair[1])
        cnt = 0
        for i, pair in enumerate(cnts):
            cnt += (i // 8 + 1) * pair[1]
        return cnt