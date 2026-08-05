class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        isPrimes = bytearray([1] * n)
        cnt = 0
        isPrimes[0] = 0
        isPrimes[4 : n : 2] = bytearray(len(range(4, n, 2)))
        for i in range(2, n):
            if not isPrimes[i]:
                continue
            cnt += 1
            isPrimes[i*i : n : 2 * i] = bytearray(len(range(i*i, n, 2 * i)))

        return cnt