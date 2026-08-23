from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start point ascending; for ties on the start point,
        # put the interval with the larger end point first (so it can "cover" the ones that follow)
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))

        count = 1
        start, end = intervals[0]

        for i in range(1, len(intervals)):
            curStart, curEnd = intervals[i]
            # If the current interval is fully contained within [start, end], it's covered -> skip it
            if start <= curStart and curEnd <= end:
                continue
            # Otherwise this interval is not covered; count it and extend the covering range
            count += 1
            start, end = min(start, curStart), max(end, curEnd)

        return count
