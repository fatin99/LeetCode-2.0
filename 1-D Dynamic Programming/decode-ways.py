class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        dp = [1]

        for i in range(1, len(s) + 1):
            result = 0
            for j in range(i):
                substring = s[j:i]
                if substring[0] == "0" or int(substring) > 26:
                    continue
                result += dp[j]
            dp.append(result)

        return dp[-1]

    #Bottom-up with Tabulation
    # def numDecodings(self, s: str) -> int:
    #     if len(s) == 0:
    #         return 0
        
    #     dp = [[] for _ in range(len(s) + 1)]
    #     dp[0] = [[""]]

    #     for i in range(1, len(s) + 1):
    #         for j in range(i):
    #             substring = s[j:i]
    #             if substring[0] == "0" or int(substring) > 26:
    #                 continue
    #             for prev in dp[j]:
    #                 if prev == [""]:
    #                     dp[i].append([substring])
    #                 else:
    #                     dp[i].append(prev + [substring])

    #     print(dp[-1])
    #     return len(dp[-1])

    # #Bottom-up without Tabulation (saves memory but not enough)
    # def numDecodings(self, s: str) -> int:
    #     dp = [[s[0]]]  

    #     for i in range(1, len(s)):
    #         newResult = []
    #         for codeSequence in dp:
    #             if s[i] != "0": # add single char s[i] to code sequence
    #                 newResult.append(codeSequence + [s[i]])
                
    #             lastCode = codeSequence[-1] + s[i] # last element of code sequenc e + char s[i]
    #             if int(lastCode) > 26:
    #                 continue
    #             newResult.append(codeSequence[:-1]+[lastCode])

    #         dp = newResult

    #     # print(result)
    #     return len(dp)
    
    # Top-down with Memoization
    # def numDecodings(self, s: str) -> int:
    #     memo = [[[s[0]]]]  
    #     def decode(n):
    #         if len(memo) > n:
    #             return memo[n]
            
    #         code = decode(n-1)
            
    #         res = []
    #         for codeSequence in code:
    #             if s[n] != "0": # add single char s[i] to code sequence
    #                 res.append(codeSequence + [s[n]])
                
    #             lastCode = codeSequence[-1] + s[n] # last element of code sequenc e + char s[i]
    #             if int(lastCode) <= 26:
    #                 res.append(codeSequence[:-1]+[lastCode])
            
    #         if len(memo) == n:
    #             memo.append(res)
            
    #         return res
        
    #     decodings = decode(len(s)-1)
    #     print(decodings)
    #     return len(decodings)

    # Top-down with Memoization
    # def numDecodings(self, s: str) -> int:
    #     memo = [[[s[0]]]]  
    #     def decode(n):
    #         if len(memo) > n:
    #             return memo[n]
            
    #         code = decode(n-1)
            
    #         res = []
    #         for codeSequence in code:
    #             if s[n] != "0": # add single char s[i] to code sequence
    #                 res.append(codeSequence + [s[n]])
                
    #             lastCode = codeSequence[-1] + s[n] # last element of code sequenc e + char s[i]
    #             if int(lastCode) <= 26:
    #                 res.append(codeSequence[:-1]+[lastCode])
            
    #         if len(memo) == n:
    #             memo.append(res)
            
    #         return res
        
    #     decodings = decode(len(s)-1)
    #     print(decodings)
    #     return len(decodings)
    
    # Top-down with DFS
    # def numDecodings(self, s: str) -> int:
    #     result = []

    #     def dfs(start, codeSequence):
    #         if start == len(s):
    #             result.append(list(codeSequence))
    #             return
            
    #         for end in range(start + 1, len(s) + 1):
    #             subStr = s[start:end]
    #             if subStr[0] == "0" or int(subStr) > 26:
    #                 continue
    #             codeSequence.append(subStr)
    #             dfs(end, codeSequence)
    #             codeSequence.pop()

    #     dfs(0, [])
    #     return len(result)

print(Solution().numDecodings("123"))
print(Solution().numDecodings("123123"))

# [[[""]], [[1]], [[1,2][12]], [[1,2,3][1,23][12,3]]]