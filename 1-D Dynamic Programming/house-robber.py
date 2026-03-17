class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) > 1:
            dp = [nums[0], nums[1]]
            prevMax = nums[0]  # tracks max of dp[0..i-2]
            
            for i in range(2, len(nums)):
                currMax = nums[i] + prevMax
                prevMax = max(prevMax, dp[-1])  # update before appending
                dp.append(currMax)
            
            return max(dp[-1], dp[-2])
        
        else:
            return max(nums)

print(Solution().rob([1,2,3,1]))
print(Solution().rob([2,7,9,3,1]))