class Solution:
    def plusOne(self, digits: list) -> list:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
    
    # Recursive solution
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]

        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            return self.plusOne(digits[:-1]) + [0]
        
# print(Solution().plusOne([1]))
# print(Solution().plusOne([9]))
# print(Solution().plusOne([1, 9, 9]))
print(Solution().plusOne([9, 9, 9]))