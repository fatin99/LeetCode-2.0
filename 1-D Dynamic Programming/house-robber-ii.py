class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_helper(nums: List[int]) -> int:
            if len(nums) >= 2:
                prev = nums[1]
                prev_prev = nums[0]
                prev_max = prev_prev
                for i in range(2, len(nums)):
                    curr = max(nums[i], nums[i] + prev_max)
                    prev_max = max(prev_max, prev)
                    prev_prev, prev = prev, curr
                return max(prev, prev_prev)
            else:
                return max(nums)

        
        if len(nums) > 3:
            return max(nums[0] + rob_helper(nums[2:-1]), 
                       nums[-1] + rob_helper(nums[1:-2]), 
                       rob_helper(nums[1:-1])
                       )
        else:
            return max(nums)

print(Solution().rob([1]))
print(Solution().rob([1,2,]))
print(Solution().rob([1,2,3]))
print(Solution().rob([1,2,3,4]))
print(Solution().rob([1,2,3,4,5]))
# print(Solution().rob([1,2,3,4,5,6,7,8,9,10]))
# print(Solution().rob([1,2,3,1]))
print(Solution().rob([200,3,140,20,10]))


