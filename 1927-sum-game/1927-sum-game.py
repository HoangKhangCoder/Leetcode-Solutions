class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)

        # Helper: for a half of the string, return the sum of its known
        # digits (digitSum) and the count of '?' characters (questionCount)
        # in that half.
        def get(half: str) -> (int, int):
            digitSum = questionCount = 0
            for ch in half:
                if ch == "?":
                    questionCount += 1
                else:
                    digitSum += int(ch)
            return digitSum, questionCount

        # Split the string into a left half and a right half
        sum0, question0 = get(num[: n // 2])
        sum1, question1 = get(num[n // 2 :])

        # Idea: Alice wants the left-half sum to equal the right-half sum,
        # while Bob wants them to differ. Alice and Bob alternately fill in
        # the '?' cells with digits 0-9.
        # - If the total number of '?' cells (question0 + question1) is odd,
        #   Bob always gets the last move and can break the balance -> Bob
        #   wins (return True).
        # - If the number of '?' cells is even: for each pair of '?' cells
        #   (one on the left, one on the right) that the two players fill in
        #   turn, the maximum difference Bob can create per pair is 9 (Alice
        #   will always balance out the rest). So Bob wins when the current
        #   sum difference (sum0 - sum1) does not match the difference Alice
        #   can compensate for, i.e. (question1 - question0) * 9 / 2.
        return (question0 + question1) % 2 == 1 or sum0 - sum1 != (question1 - question0) * 9 // 2
