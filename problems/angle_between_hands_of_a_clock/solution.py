class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minAngle = 360 // 60 * minutes
        hourAngle = (360 // 12) * (hour % 12) + (minutes * (360/12/60))
        diff = abs(minAngle - hourAngle)
        return min(diff, 360-diff)