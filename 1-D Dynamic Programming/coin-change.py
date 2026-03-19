from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        coins.sort(reverse=True) # O(1), 1 <= coins.length <= 12
        if coins[-1] > amount:
            return -1

        prevSums = [0]
        count = 1
        while True:
            currSums = set()
            for prevSum in prevSums:
                for coin in coins:
                    currSum = prevSum + coin
                    if currSum < amount:
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


coins = [2,5,1]
amount = 11
print(Solution().coinChange(coins, amount))
coins = [2]
amount = 3
print(Solution().coinChange(coins, amount))
coins = [1]
amount = 0
print(Solution().coinChange(coins, amount))
coins = [186,419,83,408]
amount = 6249
print(Solution().coinChange(coins, amount))
coins = [412,392,401,75,38,106,223]
amount = 7802
print(Solution().coinChange(coins, amount))
