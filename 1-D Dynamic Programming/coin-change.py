class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
    
        coins.sort(reverse=True) # O(1), 1 <= coins.length <= 12
        if coins[-1] > amount:
            return -1
        
        prev = [coins[0]]

        for i in range(1, len(coins)):
            result = []
            for j in range(len(prev)):
                for k in range(j, i+1):
                    currSum = coins[k]+prev[j]
                    result.append(currSum)
            if len(prev) > 1:
                result.append(int(prev[-1]/i*(i+1)))
            currSum = coins[i]*(i+1)
            result.append(currSum)
            prev = result

        print(prev)
        return -1



coins = [1,2,3,4]
amount = 11
print(Solution().coinChange(coins, amount))

# 4 3 2 1

# 5
# 55 52 22
# 555 552 551 522 521 222 221 111
