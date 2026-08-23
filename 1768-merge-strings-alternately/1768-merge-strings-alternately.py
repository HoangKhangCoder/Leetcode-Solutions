class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Idea: walk two pointers in lockstep over word1 and word2, taking one
        # character from word1 then one from word2 at each step to interleave
        # them into the result. Once one string is exhausted, append whatever
        # remains of the other string to the end.
        len1, len2 = len(word1), len(word2)
        idx = 0
        result = ""

        # Interleave characters until we reach the length of the shorter string
        while idx < min(len1, len2):
            result += word1[idx]
            result += word2[idx]
            idx += 1

        # Append the leftover tail (if any) of word1 to the result
        if idx < len1:
            result += word1[idx:]
        # Append the leftover tail (if any) of word2 to the result
        if idx < len2:
            result += word2[idx:]

        return result
