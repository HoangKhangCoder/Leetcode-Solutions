class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        longest = 2
        l = r = 0
        seen = {}
        while r < len(s):
            char = s[r]
            seen[char] = seen.get(char, 0) + 1
            while seen[char] > 2:
                seen[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
            r += 1
        return longest