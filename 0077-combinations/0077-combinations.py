class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Idea: use backtracking to generate all k-combinations of the
        # numbers from 1 to n. At each step, try adding a number to the
        # current "path", recurse further, then remove that number
        # (backtrack) to try a different one.
        result = []

        def backtrack(start, path):
            # Once path has k elements, it's a valid combination
            if len(path) == k:
                result.append(list(path))
                return

            for i in range(start, n + 1):
                path.append(i)          # choose number i
                backtrack(i + 1, path)  # recurse to keep choosing numbers greater than i
                path.pop()              # backtrack: remove i to try a different number

        backtrack(1, [])
        return result
