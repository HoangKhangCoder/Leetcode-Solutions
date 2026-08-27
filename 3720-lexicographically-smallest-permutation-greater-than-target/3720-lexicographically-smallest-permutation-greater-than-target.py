from collections import Counter
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        s_counts = Counter(s)
        
        for i in range(n - 1, -1, -1):
            prefix = target[:i]
            prefix_counts = Counter(prefix)
            
            possible = True
            for char, count in prefix_counts.items():
                if s_counts[char] < count:
                    possible = False
                    break
            
            if not possible:
                continue
                
            rem_counts = s_counts - prefix_counts
            
            target_char = target[i]
            chosen_char = None
            
            for c in range(ord(target_char) + 1, ord('z') + 1):
                char_candidate = chr(c)
                if rem_counts[char_candidate] > 0:
                    chosen_char = char_candidate
                    break
            
            if chosen_char:
                rem_counts[chosen_char] -= 1
                
                suffix_chars = []
                for c in range(ord('a'), ord('z') + 1):
                    char_candidate = chr(c)
                    if rem_counts[char_candidate] > 0:
                        suffix_chars.extend([char_candidate] * rem_counts[char_candidate])
                
                return prefix + chosen_char + "".join(suffix_chars)
                
        return ""
