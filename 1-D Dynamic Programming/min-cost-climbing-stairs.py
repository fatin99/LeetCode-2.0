from typing import List


class Solution:
    # #Bottom-up with Tabulation
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     minCost = [cost[0], cost[1]]
    #     for i in range(2, len(cost) + 1):
    #         currMinCost = min(minCost[i - 1], minCost[i - 2])
    #         if i < len(cost):
    #             currMinCost += cost[i]
    #         minCost.append(currMinCost)
    #     return minCost[-1]
    
    # Top-down with Memoization
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = [cost[0], cost[1]]

        def dp(n, memo):
            if len(memo) > n: # check for the solution in the memo, if found, return it right away
                return memo[n]
            res = min(dp(n - 1, memo), dp(n - 2, memo))
            if n < len(cost):
                res += cost[n]
            if len(memo) == n:
                memo.append(res)
            return res

        dp(len(cost) + 1, minCost)
        return minCost[-1]
    
    # DP without list
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])


print(Solution().minCostClimbingStairs([10,15,20]))
print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))