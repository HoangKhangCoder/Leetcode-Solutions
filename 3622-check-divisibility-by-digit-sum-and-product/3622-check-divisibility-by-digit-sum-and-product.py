class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digitProduct = 1
        digitSum = 0

        # Iterate over each digit of n to compute the sum and product of its digits.
        for digitChar in str(n):
            digit = int(digitChar)
            digitSum += digit
            digitProduct *= digit

        # Check whether n is divisible by (sum of digits + product of digits).
        return n % (digitSum + digitProduct) == 0
