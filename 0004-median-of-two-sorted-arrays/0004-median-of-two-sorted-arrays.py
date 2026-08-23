class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Idea: merge the two sorted arrays the way merge sort does, but
        # without ever building the full merged array. We only need to know
        # the position(s) of the middle element(s) of the merged sequence in
        # order to compute the median.
        m, n = len(nums1), len(nums2)
        i = j = 0  # pointers walking nums1 and nums2 respectively

        # If the total length is odd, the median is a single middle element,
        # so sMid == eMid. If it's even, the median is the average of the two
        # middle elements, so sMid and eMid are adjacent indices.
        sMid, eMid = (m + n) // 2 if (m + n) % 2 else (m + n) // 2 - 1, (m + n) // 2
        res = 0
        lenMid = eMid - sMid + 1  # number of elements to sum to compute the median (1 or 2)

        # Keep merging until we've passed index eMid of the merged sequence
        while i + j <= eMid:
            # Pick the smaller of nums1[i] and nums2[j] (standard merge step)
            if (not i == m) and (j == n or nums1[i] < nums2[j]):
                chosen = nums1[i]
                i += 1
            else:
                chosen = nums2[j]
                j += 1
            # If the current position in the merged sequence (i + j - 1) falls
            # within [sMid, eMid], accumulate it so we can average it later
            if i + j - 1 >= sMid:
                res += chosen
        return res / lenMid
