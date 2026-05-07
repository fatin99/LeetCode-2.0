class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]
        for i in range(1, len(nums)):
            maxLen = 1
            curr = nums[i]
            for j in range(i):
                prev = nums[j]
                if curr > prev:
                    maxLen = max(maxLen, dp[j] + 1)
            dp.append(maxLen)
        return max(dp)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(Solution().lengthOfLIS(nums))

nums = [0, 1, 0, 3, 2, 3]
print(Solution().lengthOfLIS(nums))

nums = [7, 7, 7, 7, 7, 7, 7]
print(Solution().lengthOfLIS(nums))
