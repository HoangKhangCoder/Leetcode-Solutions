class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # Sliding window technique: expand the right pointer to add elements;
        # when the frequency of the element just added exceeds k, shrink the
        # window from the left until the frequency becomes valid again. The
        # largest valid window length seen is the answer.
        leftPtr = rightPtr = 0
        result = k
        counts = {}

        while rightPtr < len(nums):
            num = nums[rightPtr]
            counts[num] = counts.get(num, 0) + 1

            # If the current element's frequency exceeds k, shrink the window from the left
            while counts[num] > k:
                counts[nums[leftPtr]] -= 1
                leftPtr += 1

            result = max(rightPtr - leftPtr + 1, result)
            rightPtr += 1

        return result
