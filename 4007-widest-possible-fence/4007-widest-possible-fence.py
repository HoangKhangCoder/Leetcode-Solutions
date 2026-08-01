class Solution:
    def maximumWidth(self, A: list[int]) -> int:
        freq = Counter(A)
        count = Counter()
        res = max(freq.values())
        for a in freq:
            for b in freq:
                if a < b:
                    count[a + b] += min(freq[a], freq[b])
                if a == b:
                    count[a + b] += freq[a] // 2
                res = max(res, freq[a + b] + count[a + b])
        return res