class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = (len(nums) * (len(nums) - 1))/2
        return sum - sum(nums)
    
    # Bitwise XOR
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n
        for i in range(n):
            xorr ^= i ^ nums[i]
        return xorr
    
    # Built-in function
    def missingNumber(self, nums: List[int]) -> int:    
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
        
print(Solution().missingNumber([3,0,1]))
