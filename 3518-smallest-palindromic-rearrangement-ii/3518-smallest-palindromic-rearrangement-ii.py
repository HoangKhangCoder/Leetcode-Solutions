from collections import Counter
from functools import cache
import math


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        counts = Counter(s)

        # Determine which characters have an odd count (at most one such
        # character is allowed for a valid palindrome) and how many of each
        # character go into one side (sideCount = count // 2, the rest
        # mirrors across the middle).
        oddChars = []
        sideCount = {}
        for char in sorted(counts.keys()):
            if counts[char] % 2 == 1:
                oddChars.append(char)
            if counts[char] // 2 > 0:
                sideCount[char] = counts[char] // 2

        # If more than one character has an odd count, no palindrome can be formed.
        if len(oddChars) > 1:
            return ""
        midChar = oddChars[0] if oddChars else ""

        @cache
        def factorial(n):
            return math.factorial(n)

        halfLength = sum(sideCount.values())

        # Compute the number of distinct arrangements (permutations with
        # repetition) of the characters in countMap, where totalN is the
        # total number of elements.
        def countArrangements(countMap, totalN):
            arrangements = factorial(totalN)
            for count in countMap.values():
                if count > 1:
                    arrangements //= factorial(count)
            return arrangements

        remainingWays = countArrangements(sideCount, halfLength)

        # If k exceeds the total number of possible arrangements, the k-th
        # palindrome doesn't exist -> return an empty string.
        if k > remainingWays:
            return ""

        # Build the first half (halfPart) greedily in alphabetical order,
        # similar to the classic "k-th permutation" algorithm: at each step,
        # try placing the smallest remaining character; if the number of
        # arrangements for that choice (ways) >= k, pick that character,
        # otherwise subtract ways from k and try the next character.
        halfPart = []
        remainingLength = halfLength

        for _ in range(halfLength):
            for char in sorted(sideCount.keys()):
                charCount = sideCount[char]
                if charCount > 0:
                    ways = (remainingWays * charCount) // remainingLength

                    if k <= ways:
                        halfPart.append(char)
                        sideCount[char] -= 1
                        remainingWays = ways
                        remainingLength -= 1
                        break
                    else:
                        k -= ways

        prefix = "".join(halfPart)
        return prefix + midChar + prefix[::-1]
