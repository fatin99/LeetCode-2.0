from collections import defaultdict

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        start = 0
        end = start
        curr = 1
        while start < len(nums) and end < len(nums):
            if nums[end] > 0:
                curr *= nums[end]
                end += 1
            elif nums[end] == 0:
                start = end+1
                end += 1
            else:

      


nums = [2,3,-2,4]
print(Solution().maxProduct(nums))

nums = [-2,0,-1]
print(Solution().maxProduct(nums))

nums = [1,2,-3,4]
print(Solution().maxProduct(nums))

nums = [-2,-1]
print(Solution().maxProduct(nums))

