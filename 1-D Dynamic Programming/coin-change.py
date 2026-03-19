class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if coins[-1] > amount:
            return -1
        
        coins.sort(reverse=True) # O(1), 1 <= coins.length <= 12
        prev = set([coins[0]])

        for i in range(1, len(coins)):
            result = []
            for index, prevSum in enumerate(prev):
                for k in range(index, i+1):
                    currSum = coins[k]+prevSum
                    result.append(currSum)
            
            if len(prev) > 1:
                result.append(int(prevSum/i*(i+1)))
            
            currSum = coins[i]*(i+1)
            result.append(currSum)
            prev = result

        print(prev)
        return -1



coins = [1,2,5]
amount = 11
print(Solution().coinChange(coins, amount))

# 4 3 2 1

# 5
# 55 52 22
# 555 552 551 522 521 222 221 111
