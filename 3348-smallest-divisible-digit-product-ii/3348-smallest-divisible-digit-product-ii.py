from functools import cache
from math import gcd


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 0: If t has any prime factor greater than 7 (i.e. it isn't
        # made up solely of the factors 2, 3, 5, 7 — the only prime factors
        # that a single digit 0-9 can contribute), then no digit product can
        # ever be divisible by t => return "-1" immediately.
        remaining = t
        for factor in range(2, 8):
            while remaining % factor == 0:
                remaining //= factor
        if remaining > 1:
            return "-1"

        n = len(num)

        # anotherDp(length, curRem): finds the SMALLEST string with exactly
        # "length" digits (unconstrained by num, i.e. it does not need to be
        # >= num) such that the product of its digits reduces the remaining
        # factor to be cancelled (curRem) down to 1 — meaning the chosen
        # digits' product is divisible by the outstanding factor of t.
        # Digits are tried from smallest (1) to largest (9) at each position
        # to guarantee the smallest possible result.
        @cache
        def anotherDp(length, curRem):
            if length == 0:
                return '' if curRem == 1 else None
            # If the remaining length is too large, pad with digit '1'
            # (which does not affect the product) to cap recursion depth /
            # cache size — only the last 50 characters need to be computed.
            if length > 50:
                suffix = anotherDp(50, curRem)
                if suffix is not None:
                    return '1' * (length - 50) + suffix
                return None
            for digit in range(1, 10):
                newRem = curRem // gcd(curRem, digit)
                suffix = anotherDp(length - 1, newRem)
                if suffix is not None:
                    return str(digit) + suffix
            return None

        # dp(i, isLimit, rem): builds a result string with exactly n digits,
        # the same length as num, such that the result >= num (satisfying the
        # "smallest number not less than num" constraint).
        # isLimit indicates whether the digits chosen so far still exactly
        # match num's prefix (once no longer constrained, we can freely pick
        # the smallest possible digits -> delegate to anotherDp).
        def dp(i, isLimit, rem):
            if i == n:
                return '' if rem == 1 else None
            if not isLimit:
                return anotherDp(n - i, rem)
            lowerBound = max(1, int(num[i]))
            for digit in range(lowerBound, 10):
                newLimit = isLimit and digit == int(num[i])
                newRem = rem // gcd(rem, digit)
                suffix = dp(i + 1, newLimit, newRem)
                if suffix is not None:
                    return str(digit) + suffix
            return None

        # First try to find a result with the same length as num (value >= num)
        result = dp(0, True, t)
        if result:
            return result

        # If none exists, keep increasing the string length until a valid result is found
        curLength = n + 1
        while True:
            result = anotherDp(curLength, t)
            if result is not None:
                return result
            curLength += 1
