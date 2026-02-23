class Solution:
    # #Bottom-up with Tabulation
    # def climbStairs(self, n: int) -> int:
    #     dp = [1, 1]
    #     for i in range(2, n + 1):
    #         dp.append(dp[i - 1] + dp[i - 2])
    #     return dp[-1]

    # Top-down with Memoization
    memo = [1, 1]
    def climbStairs(self, n):
        if len(self.memo) > n: # check for the solution in the memo, if found, return it right away
            return self.memo[n]
        res = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        if len(self.memo) == n:
            self.memo.append(res)
        return res
    
    # DP without list
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one
    
    # Fibonaccci sequence with matrix exponentiation
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        def matrix_mult(A, B):
            return [[A[0][0] * B[0][0] + A[0][1] * B[1][0],
                     A[0][0] * B[0][1] + A[0][1] * B[1][1]],
                    [A[1][0] * B[0][0] + A[1][1] * B[1][0],
                     A[1][0] * B[0][1] + A[1][1] * B[1][1]]]

        def matrix_pow(M, p):
            result = [[1, 0], [0, 1]]
            base = M

            while p:
                if p % 2 == 1:
                    result = matrix_mult(result, base)
                base = matrix_mult(base, base)
                p //= 2

            return result

        M = [[1, 1], [1, 0]]
        result = matrix_pow(M, n)
        return result[0][0]

print(Solution().climbStairs(5))

# Input: n = 4
# Output: 5 (3 + 2)
# Explanation: There are five ways to climb to the top.
# 1. 1 step + 1 step + 1 step = 3 -> + 1 step
# 2. 1 step + 2 steps = 3 -> + 1 step
# 3. 2 steps + 1 step = 3 -> + 1 step
# 4. 1 step + 1 step = 2 -> + 2 step
# 5. 2 steps = 2 -> + 2 step