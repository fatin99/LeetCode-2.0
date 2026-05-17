class Solution:
    def getSum(self, a: int, b: int) -> int:
        print(f"a: {a:32b}")
        print(f"b: {b:32b}")
        mask = (1 << 32) - 1  # any_value & mask  →  keeps only the bottom 32 bits
        while b != 0:
            # AND (&)  =  finds WHERE a carry happens,
            # << 1     =  shifts the carry into its proper column (shift left by 1)
            carry = (a & b) << 1
            print(f"c: {carry:32b}")
            a = (a ^ b) & mask  # XOR (^)  =  partial sum w/o carrying
            print(f"a: {a:32b}")
            b = carry & mask
            print(f"b: {b:32b}")

        if a > (1 << 31) - 1:  # top bit is set (negative number)
            # convert it back to a Python signed int
            a = a ^ mask  # flip the low 32 bits
            print(f"a: {a:32b}")
            a = ~a  # negate and subtract 1
            print(f"a: {a:32b}")
        return a


print(Solution().getSum(12, 23))
print(Solution().getSum(12, -23))
