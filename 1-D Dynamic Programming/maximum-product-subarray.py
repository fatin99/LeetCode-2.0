class Solution:
    # https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            temp = curMax * num
            curMax = max(temp, num * curMin, num)
            curMin = min(temp, num * curMin, num)
            result = max(result, curMax)
        return result

nums = [2,3,-2,4]
print(Solution().maxProduct(nums))

nums = [-2,0,-1]
print(Solution().maxProduct(nums))

nums = [1,2,-3,4]
print(Solution().maxProduct(nums))

nums = [-2,-1]
print(Solution().maxProduct(nums))

nums = [-2,3,-4]
print(Solution().maxProduct(nums))