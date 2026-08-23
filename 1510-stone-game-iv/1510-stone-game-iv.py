from math import isqrt

# Precompute the win/lose outcome for every value of n within the allowed range
# dp[i] = True means the player whose turn it is (with i stones remaining) will WIN
maxN = 10 ** 5
dp = [False] * (maxN + 1)
squares = [k ** 2 for k in range(1, isqrt(maxN) + 1)]

for i in range(maxN + 1):
    # If state i is already marked as a win (True), no need to process it further
    if dp[i]:
        continue
    # From losing state i, try subtracting a perfect square -> the opponent lands in a losing state,
    # meaning the player who just moved (pushing the opponent into state i) will win
    for sq in squares:
        if i + sq > maxN:
            break
        dp[i + sq] = True


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        return dp[n]
