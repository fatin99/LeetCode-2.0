from math import floor

class Solution:
    def sumOfSquares(x):
        total = 0
        while x > 0:
            digit = x % 10
            total += digit * digit
            x = floor(x/10)
        return total
    
    def isHappy(self, n: int) -> bool:
        numbers = set()
        while n != 1:
            n = self.sumOfSquares(n)
            if n in numbers:
                return False
            numbers.add(n)
        return True
    
    # Fast and Slow Pointer
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)

        while slow != fast:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(self.sumOfSquares(fast))
        return True if fast == 1 else False

print(Solution().isHappy(91))
print(Solution().isHappy(2))
print(Solution().isHappy(1))
