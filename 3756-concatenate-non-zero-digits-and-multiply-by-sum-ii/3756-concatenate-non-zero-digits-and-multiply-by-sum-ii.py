class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        mod = 10 ** 9 + 7

        # For each position i (1-indexed into the prefix arrays), store 3
        # prefix values computed over the non-zero digits of s[0..i-1]:
        #   prefixSum[i]  : sum of the non-zero digits.
        #   prefixCount[i]: count of the non-zero digits.
        #   prefixValue[i]: the "value of concatenating the non-zero digits",
        #                    represented modularly by multiplying each digit
        #                    by the modular inverse of 10^position, so that
        #                    the value over any subarray can be derived
        #                    quickly via a difference.
        prefixSum = [0] * (n + 1)
        prefixCount = [0] * (n + 1)
        prefixValue = [0] * (n + 1)

        curSum = 0
        curCount = 0
        curValue = 0
        for i in range(n):
            digit = int(s[i])
            if digit != 0:
                curSum += digit
                curCount += 1
                # Multiply digit by 10^(-curCount) (mod) so that when we
                # later combine several digits, we can "shift" the value by
                # multiplying with the appropriate power of 10.
                invPow = pow(10, -curCount, mod)
                curValue = (curValue + digit * invPow) % mod
            prefixSum[i + 1] = curSum
            prefixCount[i + 1] = curCount
            prefixValue[i + 1] = curValue

        result = []
        for left, right in queries:
            total = prefixSum[right + 1] - prefixSum[left]
            if total <= 0:
                result.append(0)
                continue

            # Difference of the "encoded" values for the range [left, right]
            # (normalized by the modular inverse computed above).
            sigma = (prefixValue[right + 1] - prefixValue[left]) % mod
            # Multiply back by 10^(number of non-zero digits from the start
            # up to right) to recover the actual concatenated value for the
            # range [left, right].
            scale = pow(10, prefixCount[right + 1], mod)
            joinedValue = (scale * sigma) % mod
            result.append((joinedValue * total) % mod)

        return result
