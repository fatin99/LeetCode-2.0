from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        coins.sort(reverse=True) # O(1), 1 <= coins.length <= 12
        if coins[-1] > amount:
            return -1
        if len(coins) == 1 and coins[0] > amount:
            return -1

        prevSums = [0]
        
        count = 1
        while True:
            currSums = []
            for i in range(len(prevSums)):
                prevSum = prevSums[i]
                for j in range(i, len(coins)):
                    coin = coins[j]
                    currSum = prevSum + coin
                    if currSum < amount:
                        currSums.append(currSum)
                    elif currSum == amount:
                        return count
            if not currSums or currSums[-1] > amount:
                return -1
            count += 1
            prevSums = currSums
        


coins = [1,2,5]
amount = 11
print(Solution().coinChange(coins, amount))
coins = [2]
amount = 3
print(Solution().coinChange(coins, amount))
coins = [1]
amount = 0
print(Solution().coinChange(coins, amount))

# 5 2 1 --> 11

# 1 coin
# 5 
# 2
# 1

# 2 coin
# 55 
# 52 
# 51
# 22
# 21
# 11 --> check if this is more than amount, if it is, return -1

# 3 coin
# 555
# 525
# 515 
# 225
# 215
# 115
# 552
# 522
# 512
# 222
# 212
# 112
# 551
# 521
# 511
# 221
# 211
# 111
