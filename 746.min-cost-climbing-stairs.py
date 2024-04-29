class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [-1] * len(cost)
        min_cost[0] = 0
        min_cost[1] = 0
        for i in range(2, len(cost)):
            minimum = min(min_cost[i - 1] + cost[i - 1], min_cost[i - 2] + cost[i - 2])
            min_cost[i] = minimum

        return min(min_cost[-1] + cost[-1], min_cost[-2] + cost[-2])
