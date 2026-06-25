class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        data = [(0, 0)]
        no = 0
        yes = 0
        for x in nums:
            if x == target:
                yes += 1
            else:
                no += 1
            data.append((yes, no))
        n = len(nums)
        cnt = 0
        for i in range(n):
            for j in range(i, n + 1):
                no = data[j][1] - data[i][1]
                yes = data[j][0] - data[i][0]
                if yes > no:
                    cnt += 1
        return cnt