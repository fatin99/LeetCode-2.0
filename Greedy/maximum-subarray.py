class Solution:
    def maxSubArray(self, nums):
        dp = list(nums)
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
        return max(dp)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray(nums))
nums = [1]
print(Solution().maxSubArray(nums))
nums = [5, 4, -1, 7, 8]
print(Solution().maxSubArray(nums))
