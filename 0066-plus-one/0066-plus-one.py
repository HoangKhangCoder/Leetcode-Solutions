class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add = 1
        n = len(digits)
        i = n - 1
        while i >= 0 and add:
            add, digits[i] = (digits[i] + add) // 10, (digits[i] + add) % 10
            i -= 1
        if add:
            digits.insert(0, add)
        return digits