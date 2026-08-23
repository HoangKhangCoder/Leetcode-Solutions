class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Step 1: Use the Sieve of Eratosthenes to find all primes in [0, right].
        isPrime = bytearray([1] * (right + 1))
        primes = []
        isPrime[0] = 0
        for i in range(2, right + 1):
            if not isPrime[i]:
                continue
            primes.append(i)
            # Mark composites: every multiple of i starting from i*i is not prime
            isPrime[i * i : right + 1 : i] = bytearray(len(range(i * i, right + 1, i)))

        # Step 2: Walk through the primes that fall within [left, right] in
        # increasing order, looking for the adjacent pair with the smallest gap.
        bestPair = [[-1, -1], float("inf")]
        for i, prime in enumerate(primes[:-1]):
            if prime < left:
                continue
            diff = primes[i + 1] - prime
            if diff < bestPair[1]:
                bestPair = [[prime, primes[i + 1]], diff]

        return bestPair[0]
