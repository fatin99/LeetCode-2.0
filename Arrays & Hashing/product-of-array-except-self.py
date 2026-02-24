class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     product = 1
    #     hasZero = False
    #     hasZeroes = False
    #     for num in nums:
    #         if num == 0:
    #             if hasZero:
    #                 hasZeroes = True
    #             hasZero = True
    #             continue
    #         product *= num
        
    #     if hasZeroes:
    #         return [0] * len(nums)

    #     result = []
    #     for num in nums:
    #         if hasZero:
    #             if num == 0:
    #                 result.append(product)
    #             else:
    #                 result.append(0)
    #         else:
    #             result.append(int(product / num))
        
    #     return result
    
    #Solution without division
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = [0] * len(nums)
        suffixProduct = [0] * len(nums)
        prefixNum = 1
        suffixNum = 1
        for i in range(0, len(nums)):
            prefixIndex = i
            prefixNum *= nums[prefixIndex]
            prefixProduct[prefixIndex] = prefixNum
            suffixIndex = len(nums)-1-i
            suffixNum *= nums[suffixIndex]
            suffixProduct[suffixIndex] = suffixNum

        result = [suffixProduct[1]]
        for i in range(1, len(nums) - 1):
            product = prefixProduct[i - 1] * suffixProduct[i + 1]
            result.append(product)
        result.append(prefixProduct[-2])
        return result
    
    # Solution using O(1) space
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result

print(Solution().productExceptSelf([1,2,4,6]))
