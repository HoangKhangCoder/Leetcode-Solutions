class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        result = [0] * (len(cost) + 1)
        cost.append(0)
        result[0] = cost[0]
        result[1] = cost[1]
        for i in range(2,len(cost)):
            result[i] = min(cost[i] + result[i-1],cost[i] + result[i-2])
        return result[-1]