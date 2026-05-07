class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0

        for i in range(len(nums)):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + nums[i])
            print(maxReach)
        return maxReach >= len(nums) - 1


nums = [2, 3, 1, 1, 4]
print(Solution().canJump(nums))
nums = [3, 2, 1, 0, 4]
print(Solution().canJump(nums))
