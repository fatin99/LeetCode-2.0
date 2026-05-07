class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(0, 32):
            bit = (n >> i) & 1
            if bit == 1:
                res |= 1 << (31 - i)
        return res


print(Solution().reverseBits(43261596))
# 43261596	00000010100101000001111010011100
# 964176192	00111001011110000010100101000000
