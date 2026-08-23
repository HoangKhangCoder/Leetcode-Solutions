from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        result = []

        # Try every contiguous substring of "123456789" as a candidate sequential-digit number
        for i in range(9):
            for j in range(i, 9):
                num = int(digits[i: j + 1])
                if num < low or num > high:
                    continue
                result.append(num)

        # Sort again since the generated numbers are not produced in increasing order
        result.sort()
        return result
