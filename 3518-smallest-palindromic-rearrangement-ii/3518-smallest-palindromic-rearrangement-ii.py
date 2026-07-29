from collections import Counter
from functools import cache
import math


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        counts = Counter(s)

        forMid = []
        sideCount = {}
        for char in sorted(counts.keys()):
            if counts[char] % 2 == 1:
                forMid.append(char)
            if counts[char] // 2 > 0:
                sideCount[char] = counts[char] // 2

        if len(forMid) > 1:
            return ""
        midChar = forMid[0] if forMid else ""

        @cache
        def getFactorial(n):
            return math.factorial(n)

        totalLen = sum(sideCount.values())

        def getTotalWays(countMap, totalN):
            res = getFactorial(totalN)
            for c in countMap.values():
                if c > 1:
                    res //= getFactorial(c)
            return res

        currentWays = getTotalWays(sideCount, totalLen)

        if k > currentWays:
            return ""

        side = []
        currLen = totalLen

        for _ in range(totalLen):
            for char in sorted(sideCount.keys()):
                charCount = sideCount[char]
                if charCount > 0:
                    ways = (currentWays * charCount) // currLen

                    if k <= ways:
                        side.append(char)
                        sideCount[char] -= 1
                        currentWays = ways
                        currLen -= 1
                        break
                    else:
                        k -= ways

        prefix = "".join(side)
        return prefix + midChar + prefix[::-1]