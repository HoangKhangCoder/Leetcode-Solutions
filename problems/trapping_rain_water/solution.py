from collections import deque
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0]
        maxRight = deque([0])
        for i in range(1, n):
            maxLeft.append(max(maxLeft[-1], height[i - 1]))
            maxRight.appendleft(max(maxRight[0], height[n - i]))

        area = 0
        for i in range(1, n - 1):
            h = height[i]
            minH = min(maxLeft[i], maxRight[i])
            area += max(0, minH - h)
        return area