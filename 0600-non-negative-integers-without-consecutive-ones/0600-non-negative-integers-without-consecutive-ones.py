from functools import cache


class Solution:
    def findIntegers(self, n: int) -> int:
        # Convert n to its binary representation (strip the "0b" prefix)
        binN = bin(n)[2:]
        length = len(binN)

        # Digit DP: build the binary number bit by bit from left to right
        # i: the bit position currently being decided
        # isTight: True if all previous bits exactly matched n (the upper bound is still active)
        # prevOne: True if the bit just placed before this one was 1 (used to avoid two consecutive 1 bits)
        @cache
        def helper(i: int, isTight: bool, prevOne: bool) -> int:
            if i == length:
                # All bits have been placed -> this forms one valid number
                return 1

            # If still tight, the current bit can be at most the corresponding bit of n
            upper = int(binN[i]) if isTight else 1
            res = 0

            for bit in range(upper + 1):
                # If the previous bit was 1 and the current bit is also 1 -> violates the constraint, skip
                if prevOne and bit == 1:
                    continue

                # Stays tight only if it was tight before and the current bit equals upper
                newTight = isTight and (bit == upper)
                res += helper(i + 1, newTight, bit == 1)

            return res

        return helper(0, True, False)
