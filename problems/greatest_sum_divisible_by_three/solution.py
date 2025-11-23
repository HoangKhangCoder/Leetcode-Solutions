class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total_sum = 0
        remain_one = []
        remain_two = []
        n = len(nums)
        for i in range(n):
            num = nums[i] 
            total_sum += num
            if num % 3 == 1:
                remain_one.append(num)
            elif num % 3 == 2:
                remain_two.append(num)
        remain_one.sort()
        remain_two.sort()
        remain = total_sum % 3
        if remain == 0:
            return total_sum
        if remain == 1:
            method_1 = 0
            if len(remain_one) >= 1:
                method_1 = total_sum - remain_one[0]
            method_2 = 0
            if len(remain_two) >= 2:
                method_2 = total_sum - (remain_two[0] + remain_two[1])
            return max(method_1, method_2)
        else:
            method_1 = 0
            if len(remain_two) >= 1:
                method_1 = total_sum - remain_two[0]
            method_2 = 0
            if len(remain_one) >= 2:
                method_2 = total_sum - (remain_one[0] + remain_one[1])
            return max(method_1, method_2)
        return 0