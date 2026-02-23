class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            n = n & (n-1)
            count+=1
        return count
    
    # Built-in function
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
    
print(Solution().hammingWeight(11))
