class Solution:
    def sumAndMultiply(self, n: int) -> int:
        try:
            # Remove every '0' digit from n, then join the remaining digits
            # into a new number (equivalent to "concatenating the non-zero digits").
            newN = int(str(n).replace("0", ""))
            # Multiply the new number by the sum of its own digits.
            return newN * sum(int(digit) for digit in str(newN))
        except Exception:
            # If removing the zeros leaves an empty string (int("") raises), return 0.
            return 0
