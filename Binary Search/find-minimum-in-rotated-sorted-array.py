class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        if nums[start] < nums[end]:
            return nums[start]
        while start < end:
            i = int((start + end) / 2)
            curr = nums[i]
            if curr < nums[i - 1]:
                return curr
            left = nums[start]
            right = nums[end]
            if curr >= left and curr >= right:
                start = i + 1
            else:
                end = i
        if end == len(nums) - 1:
            return nums[end]


print(Solution().findMin([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(Solution().findMin([2, 3, 4, 5, 6, 7, 8, 9, 1]))
print(Solution().findMin([3, 4, 5, 6, 7, 8, 9, 1, 2]))
print(Solution().findMin([4, 5, 6, 7, 8, 9, 1, 2, 3]))
print(Solution().findMin([5, 6, 7, 8, 9, 1, 2, 3, 4]))
print(Solution().findMin([6, 7, 8, 9, 1, 2, 3, 4, 5]))
print(Solution().findMin([7, 8, 9, 1, 2, 3, 4, 5, 6]))
print(Solution().findMin([8, 9, 1, 2, 3, 4, 5, 6, 7]))
print(Solution().findMin([9, 1, 2, 3, 4, 5, 6, 7, 8]))
