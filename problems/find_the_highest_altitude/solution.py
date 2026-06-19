class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        high = 0
        maxHigh = 0
        for x in gain:
            high += x
            maxHigh = max(maxHigh, high)
        return maxHigh