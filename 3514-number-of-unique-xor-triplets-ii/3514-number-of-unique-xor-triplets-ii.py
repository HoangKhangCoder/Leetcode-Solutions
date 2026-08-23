class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        # distinctValues starts as the set of distinct values in nums
        # (i.e. the "XOR of 1 element" case).
        distinctValues = set(nums)
        uniqueNums = distinctValues

        # Iterate twice to expand from "XOR of 1 element" to "XOR of 3 elements":
        #   - 1st iteration: combine with 1 more element -> set of XOR values of 2 elements.
        #   - 2nd iteration: combine with 1 more element -> set of XOR values of 3 elements.
        for _ in range(2):
            combined = set()
            for value in distinctValues:
                for num in uniqueNums:
                    combined.add(value ^ num)
            distinctValues = combined

        # The number of distinct XOR-triplet values is the size of the final set.
        return len(distinctValues)
