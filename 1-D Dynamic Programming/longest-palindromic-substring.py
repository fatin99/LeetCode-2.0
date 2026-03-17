class Solution:
    # O(n^2)
    def longestPalindrome(self, s: str) -> str:
        maxPalindrome = s[0]
        dp = []
        
        for i in range(len(s)-1):
            odd = (i, i) #centre of an odd length palindrome (e.g. babab)
            even = (i, i + 1) #centre of an even length palindrome (e.g. cddc)
            for start, end in [odd, even]:
                
                while start >= 0 and end <= len(s)-1 and s[start] == s[end]:
                    currStr = s[start:end+1]
                    start -= 1
                    end += 1
                
                if len(currStr) > len(maxPalindrome):
                    maxPalindrome = currStr
                dp.append(currStr)
        
        print(dp)
        return maxPalindrome
    
    # DP
    # def longestPalindrome(self, s: str) -> str:
    #     def isPalindrome(s: str) -> bool:
    #         # char is left pointer, back is right pointer
    #         back = len(s) - 1
    #         for char in s:
    #             if not char.isalnum():
    #                 continue
    #             while not s[back].isalnum():
    #                 back -= 1
    #             # print(f"Comparing {char.lower()} and {s[back].lower()}")
    #             if char.lower() == s[back].lower():
    #                 back -= 1
    #                 continue
    #             else:
    #                 return False
    #         return True
    
    #     maxPalindrome = s[0]
    #     for i in range(len(s)):
    #         end = s[i]
    #         for j in range(i-len(maxPalindrome)+1):
    #             start = s[j]
    #             currStr = s[j:i+1]
    #             if start == end and isPalindrome(currStr):
    #                 maxPalindrome = currStr
    #                 break
    #     return maxPalindrome
    
print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbd"))
print(Solution().longestPalindrome("cbbc"))
print(Solution().longestPalindrome("abbcccba"))
