class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # Let oddSum be the sum of the first n odd numbers (1, 3, 5, ..., 2n-1)
        # and evenSum be the sum of the first n even numbers (2, 4, 6, ..., 2n).
        # oddSum = n^2, evenSum = n^2 + n = n * (n + 1).
        # GCD(n^2, n^2 + n) = GCD(n^2, n) = n (since n always divides both,
        # and n^2 is divisible by n, so the greatest common divisor is exactly n).
        return n
