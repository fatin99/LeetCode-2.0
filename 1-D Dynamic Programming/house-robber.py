class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) >= 3:
            dp = [nums[0], nums[1], nums[2]+nums[0]]
            for i in range(3, len(nums)):
                prevMax = max(dp[i - 2], dp[i - 3])
                currMax = max(nums[i], nums[i]+prevMax)
                dp.append(currMax)
            return max(dp[-1], dp[-2])
        else:
            return max(nums)

print(Solution().rob([1,2,3,1]))
print(Solution().rob([2,7,9,3,1]))