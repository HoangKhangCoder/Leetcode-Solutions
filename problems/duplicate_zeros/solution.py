class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        possible_dups = 0
        n = len(arr) - 1
        for left in range(n + 1):
            if left > n - possible_dups:
                break
            if arr[left] == 0:
                if left == n - possible_dups:
                    arr[n] = 0
                    n -= 1
                    break
                possible_dups += 1
        last = n - possible_dups
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]