class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        res = set(nums)
        nums = res
        for _ in range(2):
            cur = set()
            for x in res:
                for num in nums:
                    cur.add(x ^ num)
            res = cur   
        return len(res)