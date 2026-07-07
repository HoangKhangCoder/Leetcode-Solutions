class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        print(intervals)
        cnt = 1
        start, end = intervals[0]
        for i in range(1, len(intervals)):
            time = intervals[i]
            if start <= time[0] and time[1] <= end:
                continue
            cnt += 1
            start, end = min(start, time[0]), max(end, time[1])
        return cnt