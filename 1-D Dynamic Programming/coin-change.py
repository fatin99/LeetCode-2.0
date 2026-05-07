from collections import deque


class Solution:
    # DP Bottom Up
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1

    # DP Top Down (Recursive DFS)
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]

            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))

            memo[amount] = res
            return res

        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins

    # DP Bottom Up (Iterative BFS)
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        coins.sort(reverse=True)  # O(1), 1 <= coins.length <= 12
        if coins[-1] > amount:
            return -1

        prevSums = [0]
        count = 1
        visited = set([0])
        while True:
            currSums = set()
            for prevSum in prevSums:
                for coin in coins:
                    currSum = prevSum + coin
                    if currSum < amount and currSum not in visited:
                        currSums.add(currSum)
                    elif currSum == amount:
                        return count
            currSums = list(currSums)
            # print(count)
            # print(currSums)
            # print()
            if not currSums:
                return -1

            count += 1
            prevSums = currSums
            visited.update(currSums)


coins = [2, 5, 1]
amount = 11
print(Solution().coinChange(coins, amount))
coins = [2]
amount = 3
print(Solution().coinChange(coins, amount))
coins = [1]
amount = 0
print(Solution().coinChange(coins, amount))
coins = [186, 419, 83, 408]
amount = 6249
print(Solution().coinChange(coins, amount))
coins = [412, 392, 401, 75, 38, 106, 223]
amount = 7802
print(Solution().coinChange(coins, amount))
