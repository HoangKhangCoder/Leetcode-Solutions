class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        if not occupiedIntervals:
            return []
    
        occupiedIntervals.sort()
    
        merged = []
        for start, end in occupiedIntervals:
            if not merged or start > merged[-1][1] + 1:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
    
        result = []
        for s, e in merged:
            if s < freeStart:
                result.append([s, min(e, freeStart - 1)])
            if e > freeEnd:
                result.append([max(s, freeEnd + 1), e])
    
        return result