class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        dp = [[] for _ in range(len(s) + 1)]
        dp[0] = [[""]]

        for i in range(1, len(s) + 1):
            for j in range(i):
                substring = s[j:i]
                if substring[0] == "0" or int(substring) > 26:
                    continue
                for prev in dp[j]:
                    if prev == [""]:
                        dp[i].append([substring])
                    else:
                        dp[i].append(prev + [substring])

        print(dp[-1])
        return len(dp[-1])


print(Solution().numDecodings("123123"))

# [[[""]], [[1]], [[1,2][12]], [[1,2,3][1,23][12,3]]]