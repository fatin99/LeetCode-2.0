import string

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seenChars = set()
        maxLength = 0
        start = 0
        end = 0
        while end < len(s):
            if s[end] in seenChars:
                seenChars.remove(s[start])
                start += 1
            else:
                seenChars.add(s[end])
                end += 1
                maxLength = max(maxLength, end - start)
        return maxLength
                
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     if not s:
    #         return 0
    #     for length in range(len(s), 0, -1):
    #         seenChars = set()
    #         start = 0
    #         while start <= len(s) - length:
    #             count = 0
    #             for i in range(0, length):
    #                 currChar = s[start+i]
    #                 if currChar in seenChars:
    #                     start += 1
    #                     seenChars.clear()
    #                     break
    #                 else:
    #                     seenChars.add(currChar)
    #                     count += 1
    #             if count == length:
    #                 return length


    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     if not s:
    #         return 0
    #     length = 1
    #     seenChars = set()
    #     seenChars.add(s[0])
    #     currLength = 1
    #     currStr = s[0]
    #     i = 1
    #     while i < len(s):
    #         char = s[i]
    #         if char in seenChars:
    #             seenChars.clear()
    #             if len(currStr) > 1:
    #                 seenChars.add(currStr[1])
    #                 currStr = currStr[1]
    #             else:
    #                 seenChars.add(currStr[0])
    #                 currStr = char
    #             i -= (currLength - 2)
    #             currLength = 1
    #         else:
    #             currLength += 1
    #             length = max(length, currLength)
    #             seenChars.add(char)
    #             currStr += char
    #             i += 1
    #     return length
        
print(Solution().lengthOfLongestSubstring("abcabcbb")) #3
print(Solution().lengthOfLongestSubstring("bbbbb")) #1
print(Solution().lengthOfLongestSubstring("pwwkew")) #3
print(Solution().lengthOfLongestSubstring("aab")) #2
print(Solution().lengthOfLongestSubstring(" ")) #1
print(Solution().lengthOfLongestSubstring("ab")) #2
print(Solution().lengthOfLongestSubstring("a")) #1
print(Solution().lengthOfLongestSubstring("dvdf")) #3


