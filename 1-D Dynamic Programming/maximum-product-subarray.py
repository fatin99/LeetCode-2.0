class Solution:
    # https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm
    def maxProduct(self, N, K) -> int:
        maxLiquid = int((N * (N + 1)) / 2)
        if K > maxLiquid:
            return -1

        start = 1
        end = N
        result = N

        while start < end:
            curr = int((start + end) / 2)
            remaining = N - curr
            currLiquid = maxLiquid - int(((remaining) * (remaining + 1)) / 2)
            if currLiquid >= K:
                result = curr
                end = curr
            else:
                start = curr + 1

        return result


print(Solution().maxProduct(5, 8))
print(Solution().maxProduct(4, 10))
print(Solution().maxProduct(1, 2))
print(Solution().maxProduct(10, 5))
