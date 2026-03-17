class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) > 2:
            dp0 = [nums[0], nums[1]]          
            dp1 = [nums[1], nums[2]] 
            prev_max0 = nums[0]
            prev_max1 = nums[1]

            for i in range(2, len(nums)-1):
                # dp0: only update for i < len(nums)-1 (exclude last house)
                currMax = nums[i] + prev_max0
                prev_max0 = max(prev_max0, dp0[-1])
                dp0.append(currMax)

                # dp1: only update for i >= 2 but using nums[i] offset by 1 (exclude first house)
                currMax = nums[i+1] + prev_max1
                prev_max1 = max(prev_max1, dp1[-1])
                dp1.append(currMax)

            max0 = max(dp0[-1], dp0[-2])
            max1 = max(dp1[-1], dp1[-2])
            return max(max0, max1)
        
        else:
            return max(nums)
        
    def rob(self, nums: List[int]) -> int:
        if len(nums) > 2:
            prev0 = nums[1]
            prev_prev0 = nums[0]
            prev1 = nums[2]
            prev_prev1 = nums[1]
            
            prevMax0 = prev_prev0
            prevMax1 = prev_prev1
            
            for i in range(2, len(nums)-1):
                curr = nums[i] + prevMax0
                prevMax0 = max(prevMax0, prev0)
                prev_prev0, prev0 = prev0, curr

                curr = nums[i+1] + prevMax1
                prevMax1 = max(prevMax1, prev1)
                prev_prev1, prev1 = prev1, curr
            
            max0 =  max(prev_prev0, prev0)
            max1 =  max(prev_prev1, prev1)
            return max(max0, max1)
        
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


