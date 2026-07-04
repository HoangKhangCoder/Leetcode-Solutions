class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        n = len(nums)
        cnt = 0
        pre = [0] + list(accumulate(nums))
        for i in range(n):
            for j in range(i, n):
                s = pre[j + 1] - pre[i]
                if int(str(s)[0]) == x and s % 10 == x:
                    cnt += 1
        return cnt