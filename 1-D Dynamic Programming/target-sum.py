from collections import defaultdict

class Solution:
     # DP Bottom Up (Iterative BFS)
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums.sort(reverse=True) # O(1), 1 <= nums.length <= 20  
        totalSum = sum(nums)
        if target > totalSum or target < -totalSum:
            return 0 

        prevSums = {0: 1}
        for i in range(0, len(nums)):
            currSums = defaultdict(int)
            nextSums = sum(nums[i:])
            for prevSum, ways in prevSums.items():
                add = prevSum + nextSums
                if target <= add:
                    currSum = prevSum + nums[i]
                    currSums[currSum] += ways

                subtract = prevSum - nextSums
                if target >= subtract:
                    currSum = prevSum - nums[i]
                    currSums[currSum] += ways
            prevSums = currSums 
        return prevSums.get(target, 0)

     # Best Solution: DP Bottom Up (Iterative BFS) with extra pruning on both bounds
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums.sort(reverse=True) # O(1), 1 <= nums.length <= 20  
        totalSum = sum(nums)
        if target > totalSum or target < -totalSum:
            return 0 

        prevSums = {0: 1}
        for i in range(0, len(nums)):
            currSums = defaultdict(int)
            nextSums = sum(nums[i+1:])
            for prevSum, ways in prevSums.items():
                add = prevSum + nums[i]
                if target <= add + nextSums and target >= add - nextSums:
                    currSums[add] += ways

                subtract = prevSum - nums[i]
                if target <= subtract + nextSums and target >= subtract - nextSums:
                    currSums[subtract] += ways
            prevSums = currSums 
        return prevSums.get(target, 0)
    
nums = [1]
target = 1
print(Solution().findTargetSumWays(nums, target))

nums = [1,0]
target = 1
print(Solution().findTargetSumWays(nums, target))
    
nums = [1,1,1,1,1]
target = 3
print(Solution().findTargetSumWays(nums, target))
    