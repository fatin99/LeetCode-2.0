class Solution:
    #Greedy Solution
    # def maxProfit(self, prices: List[int]) -> int:
    #     start = 0 
    #     end = 1
    #     profit = 0
    #     while end < len(prices):
    #         buy = prices[start]
    #         sell = prices[end]
    #         if buy < sell:
    #             profit = max(profit, sell - buy)
    #         else:
    #             start = end
    #         end += 1
    #     return profit
    
    #DP Solution
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for sell in prices:
            profit = max(profit, sell - buy)
            buy = min(buy, sell)
        return profit


print(Solution().maxProfit([7,1,5,0,6,4]))
print(Solution().maxProfit([7,6,4,3,1]))
print(Solution().maxProfit([1,4,2]))
print(Solution().maxProfit([2,1,2,1,0,0,1]))

