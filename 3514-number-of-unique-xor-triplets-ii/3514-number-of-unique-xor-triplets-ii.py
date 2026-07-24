class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        uniNums = list(set(nums))
        uniques = uniNums[:]
        n = len(uniNums)
        for _ in range(2):
            temp = set()
            for i in range(len(uniques)):
                for j in range(n):
                    temp.add(uniNums[j] ^ uniques[i])
            uniques = list(temp)
        return len(uniques)