from math import ceil
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = [1]
        for i in range(1, n + 1):
            fact.append(fact[-1] * i)
        left = [str(i) for i in range(1, n + 1)]

        def find(k: int):
            if k == 1:
                return "".join(left)
            groupLen = fact[len(left) - 1]
            idx = ceil(k / groupLen) - 1
            d = left[ceil(k / groupLen) - 1]
            del left[idx]
            return d + find(k - idx * groupLen)
        
        return find(k)