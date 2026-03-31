class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = []
        for _ in range(len(text1) + 1):
            dp.append([0] * (len(text2) + 1))
        
        currMax = 0
        for i in range(1, len(text1) + 1):
            curr1 = text1[i - 1]
            for j in range(1, len(text2) + 1):
                curr2 = text2[j - 1]
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    print(f"index1: {i} and curr1: {curr1} , index2: {j} and curr2: {curr2}")
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[len(text1)][len(text2)]

print(Solution().longestCommonSubsequence("abcde", "ace")) # p vs qr
print(Solution().longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypyp")) # p vs qr
print(Solution().longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd")) # hbgc 0679
