from collections import Counter


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        # Only each stone's remainder mod 3 determines the outcome of the
        # game, since whether the running total becomes divisible by 3
        # depends solely on the remainders chosen so far.
        # counts[0], counts[1], counts[2] are the number of stones with
        # remainder 0, 1, 2 respectively.
        counts = Counter(stone % 3 for stone in stones)

        if counts[0] % 2 == 0:
            # An even count of remainder-0 stones does not affect whose turn
            # it is (Alice and Bob take turns picking them up, and the total
            # turn parity is unchanged). Alice wins when both remainder-1 and
            # remainder-2 groups have at least one stone, forcing Bob to
            # always be the one who makes the running sum divisible by 3 first.
            return min(counts[1], counts[2]) > 0

        # An odd count of remainder-0 stones flips Alice's and Bob's turn
        # order once; Alice wins when the difference between the remainder-1
        # and remainder-2 counts is greater than 2.
        return abs(counts[1] - counts[2]) > 2
