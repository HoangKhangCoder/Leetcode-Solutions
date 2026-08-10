from math import isqrt
maxN = 10 ** 5
dp = [False] * (maxN + 1)
squares = [k ** 2 for k in range(1, isqrt(maxN) + 1)]
for i in range(maxN + 1):
    if dp[i]:
        continue
    for sq in squares:
        if i + sq > maxN:
            break
        dp[i + sq] = True
        
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        return dp[n]