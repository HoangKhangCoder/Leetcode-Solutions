from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        # Greedy idea: count how often each character appears, then assign
        # the most frequent characters to the keys that require the fewest
        # pushes. There are 8 available keys (2-9), and each key can be
        # assigned multiple characters requiring 1, 2, 3, ... pushes in turn.
        # Sort frequencies in descending order and split them into chunks of
        # 8 characters: the first chunk (8 most frequent characters) only
        # needs 1 push each, the second chunk needs 2 pushes each, and so on.
        counts = sorted(Counter(word).items(), key=lambda pair: -pair[1])
        totalPushes = 0
        for i, (_, freq) in enumerate(counts):
            totalPushes += (i // 8 + 1) * freq
        return totalPushes
