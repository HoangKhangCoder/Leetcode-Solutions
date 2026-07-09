import gc
gc.disable()

class Solution:
    def findIntegers(self, n: int) -> int:
        bin_n = bin(n)[2:]
        length = len(bin_n)

        @lru_cache(None)
        def helper(i: int, is_tight: bool, prev_one: bool) -> int:
            if i == length:
                return 1

            upper = int(bin_n[i]) if is_tight else 1
            res = 0
            
            for bit in range(upper + 1):
                if prev_one and bit == 1:
                    continue

                new_tight = is_tight and (bit == upper)
                res += helper(i + 1, new_tight, bit == 1)
                
            return res
        
        return helper(0, True, False)