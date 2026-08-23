class Solution:
    def countPrimes(self, n: int) -> int:
        # Idea: use the Sieve of Eratosthenes to count the number of primes
        # less than n. Mark the multiples of each prime as composite
        # (not prime).
        if n <= 1:
            return 0
        isPrimes = bytearray([1] * n)  # isPrimes[i] = 1 means i might be prime
        cnt = 0
        isPrimes[0] = 0  # 0 is not prime

        # Pre-mark all even numbers >= 4 as composite (except 2 itself)
        isPrimes[4 : n : 2] = bytearray(len(range(4, n, 2)))

        for i in range(2, n):
            if not isPrimes[i]:
                continue
            cnt += 1
            # Mark the odd multiples of i (starting at i*i) as composite.
            # The step is 2*i because the even multiples of i were already
            # eliminated above.
            isPrimes[i*i : n : 2 * i] = bytearray(len(range(i*i, n, 2 * i)))

        return cnt