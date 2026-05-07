class Solution:
    def countBits(self, n: int) -> List[int]:
        wordbits = [0] * (n + 1)
        for i in range(1, n + 1):
            wordbits[i] = wordbits[i >> 1] + (i & 1)
        return wordbits


print(Solution().countBits(5))

# int i;
#     for (i = 1; sizeof wordbits / sizeof *wordbits > i; ++i)
#         wordbits [i] = wordbits [i >> 1] + (1 & i);
