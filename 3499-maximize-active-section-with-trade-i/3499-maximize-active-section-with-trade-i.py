class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        prefix = []
        oneCon = zeroCon = 0
        ones = 0
        conGroups = 0
        for d in s:
            if d == "0":
                zeroCon -= 1
                if oneCon > 0:
                    prefix.append(oneCon)
                    conGroups += 1
                oneCon = 0
            else:
                if zeroCon < 0:
                    prefix.append(zeroCon)
                    conGroups += 1
                oneCon += 1
                ones += 1
                zeroCon = 0
        prefix.append([zeroCon, oneCon][int(s[-1])])
        conGroups += 1
        maxWay = ones
        for i in range(conGroups - 2):
            if prefix[i] > 0:
                continue
            actives = abs(prefix[i]) + abs(prefix[i + 2]) + ones
            maxWay = max(maxWay, actives)
        return maxWay