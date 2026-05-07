import math


class Solution:
    # O(n^2)
    def longestPalindrome(self, s: str) -> str:
        maxPalindrome = s[0]
        dp = []

        def findPalindrome(start, end):
            currStr = ""
            while start >= 0 and end <= len(s) - 1 and s[start] == s[end]:
                currStr = s[start : end + 1]
                start -= 1
                end += 1
            return currStr

        for i in range(len(s) - 1):
            # start from centre of an odd length palindrome (e.g. babab)
            oddStr = findPalindrome(i, i)
            # start from centre of an even length palindrome (e.g. cddc)
            evenStr = findPalindrome(i, i + 1)
            maxStr = max(oddStr, evenStr, key=len)

            if len(maxStr) > len(maxPalindrome):
                maxPalindrome = maxStr
            dp.append(maxStr)

        print(dp)
        return maxPalindrome

    # Manacher's algorithm
    def longestPalindrome(self, s: str) -> str:
        def manacher(s):
            # Preprocessing the string so that all palindromes become odd-length
            # For input string: s = "abba"
            # Transformed string ms: "@#a#b#b#a#$"
            t = "#" + "#".join(s) + "#"

            # palindromes[i] stores the radius (number of characters on one side) of the
            # longest palindrome centered at position i
            palindromes = [0] * len(t)

            start, end = 0, 0
            for i in range(len(t)):
                palindromes[i] = 0
                if i < end:
                    palindromes[i] = min(end - i, palindromes[start + (end - i)])

                while (
                    i + palindromes[i] + 1 < len(t)
                    and i - palindromes[i] - 1 >= 0
                    and t[i + palindromes[i] + 1] == t[i - palindromes[i] - 1]
                ):
                    palindromes[i] += 1

                if i + palindromes[i] > end:
                    start, end = i - palindromes[i], i + palindromes[i]

            return palindromes

        palindromes = manacher(s)
        resultLen = 0
        centerIdx = None
        for index, radius in enumerate(palindromes):
            if radius >= resultLen:
                resultLen = radius
                centerIdx = index

        resultIdx = math.floor((centerIdx - resultLen) / 2)
        return s[resultIdx : resultIdx + resultLen]


print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbd"))
print(Solution().longestPalindrome("cbbc"))
print(Solution().longestPalindrome("abbcccba"))
print(1 / 2)
