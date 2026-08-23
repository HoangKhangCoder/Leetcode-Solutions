from collections import Counter


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # Count how many times each character appears in s.
        charCounts = Counter(s)
        sortedChars = sorted(set(s))

        halfPart = ""   # first half of the palindrome (built in ascending order to be as small as possible)
        midPart = ""    # the middle character (if the string length is odd)

        # Iterate over characters in ascending order to guarantee the first
        # half is the smallest possible (greedy: smaller characters go first).
        for char in sortedChars:
            count = charCounts[char]
            # If a character's count is odd, the single leftover character
            # goes in the middle of the palindrome.
            midPart += char * (count % 2)
            # Half of the character's count (count // 2) is placed in the first half.
            halfPart += char * (count // 2)

        # The smallest palindrome = first half + middle character + reversed first half.
        return halfPart + midPart + halfPart[::-1]
