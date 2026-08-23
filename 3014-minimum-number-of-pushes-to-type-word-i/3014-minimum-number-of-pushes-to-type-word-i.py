class Solution:
    def minimumPushes(self, word: str) -> int:
        # The keypad has 8 letter keys (2-9), each of which can be assigned
        # several letters. Since the problem gives no letter-frequency
        # information to optimize against, the best we can do is spread the
        # word's characters evenly: the first 8 characters (by position) cost
        # 1 push each, the next 8 cost 2 pushes each, and so on. The formula
        # below computes the total pushes directly from the word length (n)
        # by grouping characters into chunks of 8, where each subsequent
        # chunk costs one more push per character than the previous chunk.
        n = len(word)
        fullGroups = n // 8
        return 8 * (fullGroups * (fullGroups + 1) // 2) + (n % 8) * (fullGroups + 1)
