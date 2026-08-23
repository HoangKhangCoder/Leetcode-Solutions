class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Idea: add 1 to a large integer represented as an array of digits.
        # Walk from the last digit (the units place) toward the front,
        # adding the carry into each digit, and stop early once there's no
        # carry left.
        add = 1  # the amount to add, starts as 1, then acts as the carry
        n = len(digits)
        i = n - 1
        while i >= 0 and add:
            add, digits[i] = (digits[i] + add) // 10, (digits[i] + add) % 10
            i -= 1
        # If there's still a carry after walking through the whole array
        # (e.g. 999 + 1 = 1000), insert a new digit at the front
        if add:
            digits.insert(0, add)
        return digits