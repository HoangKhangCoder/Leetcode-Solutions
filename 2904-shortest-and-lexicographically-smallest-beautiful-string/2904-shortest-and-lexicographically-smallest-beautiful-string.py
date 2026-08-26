class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones_indices = [i for i, char in enumerate(s) if char == "1"]

        if len(ones_indices) < k:
            return ""

        res = ""
        min_len = float("inf")

        for i in range(len(ones_indices) - k + 1):
            left = ones_indices[i]
            right = ones_indices[i + k - 1]

            current_sub = s[left : right + 1]
            current_len = len(current_sub)

            if current_len < min_len:
                min_len = current_len
                res = current_sub
            elif current_len == min_len:
                if current_sub < res:
                    res = current_sub

        return res
