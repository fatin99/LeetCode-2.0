import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        while start < end:
            index = int((start + end) / 2)
            if nums[index] > target:
                end = index
            if nums[index] < target:
                start = index + 1
            if nums[index] == target:
                return index
        return -1

        # Python Built-In bisect
        # index = bisect.bisect_left(nums, target)
        # return index if index < len(nums) and nums[index] == target else -1
    
print(Solution().search([-1,0,3,5,9,12], 2))
