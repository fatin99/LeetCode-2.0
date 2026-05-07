class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = num ^ res
        return res


print(Solution().singleNumber([4, 1, 2, 1, 2]))
