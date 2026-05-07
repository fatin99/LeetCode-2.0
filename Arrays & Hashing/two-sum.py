class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        count = 0  # the index of the num in nums
        for num in nums:  # Alt: for i, num in enumerate(nums) where count = 1
            remainder = target - num
            if remainder in numMap:
                return [numMap[remainder], count]
            numMap[num] = count
            count += 1
