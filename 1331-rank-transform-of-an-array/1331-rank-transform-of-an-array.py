class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortLs = sorted(set(arr))
        ranking = {}
        for i, x in enumerate(sortLs):
            ranking[x] = i + 1
        res = []
        for x in arr:
            res.append(ranking[x])
        return res