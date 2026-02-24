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
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = []
        suffixProduct = []
        prefixNum = 1
        suffixNum = 1
        for i in range(0, len(nums)):
            prefixNum *= nums[i]
            prefixProduct.append(prefixNum)
            suffixNum *= nums[-(i + 1)]
            suffixProduct.append(suffixNum)

        result = [suffixProduct[1]]
        for i in range(1, len(nums) - 1):
            product = prefixProduct[i - 1] * suffixProduct[i + 1]
            result.append(product)
        result.append(prefixProduct[-1])
        return result

print(Solution().productExceptSelf([1,2,3,4]))
