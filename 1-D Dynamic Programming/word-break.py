class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def findWord(word, start, end):
            if end in memo:
                return memo[end]
            if s[start:end] == word:
                if end == len(s):
                    return True
                elif end > len(s):
                    memo[end] = False
                    return False
                else:
                    for word in wordDict:
                        if findWord(word, end, len(word)+end):
                            return True
                    memo[end] = False
                    return False
            else:
                return False

        for word in wordDict:
            if findWord(word, 0, len(word)):
                return True
        return False
    
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     memo = {}

    #     def findWord(word, start, end):
    #         if (start, end) in memo:
    #             return memo[(start, end)]
    #         if s[start:end] == word:
    #             if end == len(s):
    #                 memo[(start, end)] = True
    #                 return True
    #             elif end > len(s):
    #                 memo[(start, end)] = False
    #                 return False
    #             else:
    #                 for word in wordDict:
    #                     if findWord(word, end, len(word)+end):
    #                         memo[(end, len(word)+end)] = True
    #                         return True
    #                 memo[(start, end)] = False
    #                 return False
    #         else:
    #             return False

    #     for word in wordDict:
    #         if findWord(word, 0, len(word)):
    #             memo[(0, len(word))] = True
    #             return True
    #     return False
    
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     wordDictSet = set(wordDict)
    #     minLen = 21
    #     maxLen = 0                                                     
    #     for word in wordDict:
    #         minLen = min(minLen, len(word))
    #         maxLen = max(maxLen, len(word))
    #     minLen -= 1
    #     maxLen = min(len(s), maxLen)

    #     memo = {}

    #     def findWord(currStr, start, end):
    #         if (start, end) in memo:
    #             return memo[(start, end)]
    #         if currStr in wordDictSet:
    #             if end == len(s):
    #                 memo[(start, end)] = True
    #                 return True
    #             else:
    #                 newEnd = min(len(s), end + maxLen)
    #                 currStr = s[end:newEnd]
    #                 for newLen in range(newEnd, end + minLen, -1):
    #                     if findWord(currStr, end, newLen):
    #                         memo[(end, newLen)] = True
    #                         return True
    #                     currStr = currStr[:-1]
    #                 memo[(start, end)] = False
    #                 return False
    #         else:
    #             memo[(start, end)] = False
    #             return False

    #     currStr = s[0:maxLen]
    #     for end in range(maxLen, minLen, -1):
    #         if findWord(currStr, 0, end):
    #             memo[(0, end)] = True
    #             return True
    #         currStr = currStr[:-1]
    #     return False

# s = "leetcode"
# wordDict = ["leet","code"]
# print(Solution().wordBreak(s, wordDict))

# s = "applepenapple"
# wordDict = ["apple","pen"]
# print(Solution().wordBreak(s, wordDict))

# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]
# print(Solution().wordBreak(s, wordDict))

# s = "bb"
# wordDict = ["a","b","bbb","bbbb"]
# print(Solution().wordBreak(s, wordDict))

# s ="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
# wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
# print(Solution().wordBreak(s, wordDict))

# s ="abcd"
# wordDict =["a","abc","b","cd"]
# print(Solution().wordBreak(s, wordDict))


s ="cars"
wordDict =["car","ca","rs"]
print(Solution().wordBreak(s, wordDict))
