class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i = 1
        res = []
        push = "Push"
        wordPop = "Pop"
        for num in target:
            while i < num:
                res.append(push)
                res.append(wordPop)
                i += 1
            res.append(push)
            i += 1
        return res