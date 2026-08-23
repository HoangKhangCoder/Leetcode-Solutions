class Solution:
    def trailingZeroes(self, n: int) -> int:
        # Idea: the number of trailing zeroes in n! equals the number of
        # times 10 appears in the prime factorization of n!, and 10 = 2 * 5.
        # Since the count of factor 2 is always greater than or equal to the
        # count of factor 5, we only need to count the factors of 5:
        # that's n/5 + n/25 + n/125 + ...
        cnt = 0
        while n > 0:
            n //= 5
            cnt += n
        return cnt