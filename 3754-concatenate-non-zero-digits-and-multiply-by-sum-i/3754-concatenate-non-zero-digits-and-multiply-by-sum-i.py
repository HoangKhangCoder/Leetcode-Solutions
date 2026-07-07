class Solution:
    def sumAndMultiply(self, n: int) -> int:
        try:
            newN = int(str(n).replace("0", ""))
            return newN * sum(int(d) for d in str(newN))
        except:
            return 0