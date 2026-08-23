class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        # A number is called "almost missing" if it appears in EXACTLY ONE
        # subarray window of size k (i.e. it only falls inside 1 window
        # starting position). For each window of size k, take the set of
        # distinct values in it (deduping within the same window) and count
        # how many windows each value appears in.
        counts = {}
        for i in range(len(nums) - k + 1):
            for num in set(nums[i : i + k]):
                counts[num] = counts.get(num, 0) + 1

        # Scan all values that appear in exactly 1 window, tracking the largest one
        result = -1
        for value, windowCount in counts.items():
            if windowCount > 1:
                continue
            result = max(result, value)

        return result
