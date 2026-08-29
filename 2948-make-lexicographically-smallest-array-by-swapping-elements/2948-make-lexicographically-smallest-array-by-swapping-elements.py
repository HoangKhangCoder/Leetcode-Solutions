class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups = []
        sortNums = sorted(nums)
        curGroup = []
        kindsDict = {}
        idxGroup = 0
        for num in sortNums:
            if curGroup and curGroup[-1] + limit < num:
                groups.append(curGroup)
                idxGroup += 1
                curGroup = []
            curGroup.append(num)
            kindsDict[num] = idxGroup
        if curGroup:
            groups.append(curGroup)
        idxCurGroup = [0] * (idxGroup + 1)
        res = []
        for num in nums:
            group = kindsDict[num]
            res.append(groups[group][idxCurGroup[group]])
            idxCurGroup[group] += 1
        return res