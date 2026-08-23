from collections import Counter


class Solution:
    def maximumWidth(self, A: list[int]) -> int:
        # freq[a]: number of posts with height a.
        freq = Counter(A)
        # pairCount[s]: number of pairs of posts (not counting a 3rd or later
        # post) whose combined height equals s, formed from either two
        # different heights or two posts of the same height.
        pairCount = Counter()

        # The smallest possible result is using only posts that already
        # share one height (no pairing needed), i.e. the maximum value in freq.
        result = max(freq.values())

        for heightA in freq:
            for heightB in freq:
                if heightA < heightB:
                    # Pair two posts of different heights: the maximum
                    # number of such pairs is limited by whichever height has fewer posts.
                    pairCount[heightA + heightB] += min(freq[heightA], freq[heightB])
                if heightA == heightB:
                    # Pair two posts of the same height: every 2 posts form 1 pair.
                    pairCount[heightA + heightB] += freq[heightA] // 2

                # The total possible width at combined height (heightA +
                # heightB) equals the posts already at that height plus the
                # pairs formed whose combined height equals it.
                combinedHeight = heightA + heightB
                result = max(result, freq[combinedHeight] + pairCount[combinedHeight])

        return result
