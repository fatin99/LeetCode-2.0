class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        hasZero = False
        hasZeroes = False
        for num in nums:
            if num == 0:
                if hasZero:
                    hasZeroes = True
                hasZero = True
                continue
            product *= num
        
        if hasZeroes:
            return [0] * len(nums)

        result = []
        for num in nums:
            if hasZero:
                if num == 0:
                    result.append(product)
                else:
                    result.append(0)
            else:
                result.append(int(product / num))
        
        return result
        