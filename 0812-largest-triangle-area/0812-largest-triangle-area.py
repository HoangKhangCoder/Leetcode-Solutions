class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        maxArea = 0.0
        n = len(points)

        # Try every triple of points (brute force) to find the triangle with the largest area
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]

                    # Compute the triangle's area from its 3 vertex coordinates (shoelace formula)
                    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

                    if area > maxArea:
                        maxArea = area

        return maxArea
