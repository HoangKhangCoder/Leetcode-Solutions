class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # Sliding window technique: expand the right pointer to add characters
        # to the window; if any character occurs more than twice in the
        # window, shrink from the left until every character occurs at most
        # twice. The largest valid window length seen during the scan is the answer.
        longest = 2
        leftPtr = rightPtr = 0
        charCount = {}

        while rightPtr < len(s):
            char = s[rightPtr]
            charCount[char] = charCount.get(char, 0) + 1

            while charCount[char] > 2:
                charCount[s[leftPtr]] -= 1
                leftPtr += 1

            longest = max(longest, rightPtr - leftPtr + 1)
            rightPtr += 1

        return longest
