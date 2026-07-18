class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        i = j = 0
        sMid, eMid = (m + n) // 2 if (m + n) % 2 else (m + n) // 2 - 1, (m + n) // 2
        res = 0
        lenMid = eMid - sMid + 1
        while i + j <= eMid:
            if (not i == m) and (j == n or nums1[i] < nums2[j]):
                chose = nums1[i]
                i += 1
            else:
                chose = nums2[j]
                j += 1
            if i + j - 1 >= sMid:
                res += chose
        return res / lenMid
