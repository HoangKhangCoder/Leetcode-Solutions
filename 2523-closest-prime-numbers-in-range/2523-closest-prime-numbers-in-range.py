class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        isPrimes = bytearray([1] * (right + 1))
        primes = []
        isPrimes[0] = 0
        for i in range(2, right + 1):
            if not isPrimes[i]:
                continue
            primes.append(i)
            isPrimes[i*i : right + 1 : i] = bytearray(len(range(i*i, right + 1, i)))
        minCoup = [[-1, -1], float("inf")]

        for i, x in enumerate(primes[:-1]):
            if x < left:
                continue
            diff = primes[i + 1] - x
            if diff < minCoup[1]:
                minCoup = [[x, primes[i + 1]], diff]
        return minCoup[0]