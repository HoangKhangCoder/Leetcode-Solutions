class Solution:
    def mySqrt(self, x: int) -> int:
        minN, maxN = 0, x
        while minN <= maxN:
            mid = (minN + maxN) // 2
            val = mid ** 2
            if val <= x and (mid + 1) ** 2 > x:
                return mid
            if val < x:
                minN = mid + 1
            else:
                maxN = mid - 1
        return