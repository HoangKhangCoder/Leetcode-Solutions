from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Take the distinct values and sort them ascending to determine ranks
        sortedUnique = sorted(set(arr))

        # Assign a rank to each value (starting from 1)
        ranking = {}
        for i, value in enumerate(sortedUnique):
            ranking[value] = i + 1

        # Map each element in the original array to its corresponding rank
        result = []
        for value in arr:
            result.append(ranking[value])

        return result
