import math

class Solution:
    # O(n^2)
    def countSubstrings(self, s: str) -> int:
        dp = []
        
        def findPalindrome(start, end):
            currStr = ""
            palindrome = 0
            while start >= 0 and end <= len(s)-1 and s[start] == s[end]:
                currStr = s[start:end+1]
                dp.append(currStr)
                palindrome += 1
                start -= 1
                end += 1
            return palindrome

        result = 0
        for i in range(len(s)):
            #start from centre of an odd length palindrome (e.g. babab)
            result += findPalindrome(i,i) 
            #start from centre of an even length palindrome (e.g. cddc)  
            if i < len(s):      
                result += findPalindrome(i,i+1)      
        
        print(dp)
        return result    
    
    # (Manacher's algorithm)
    def countSubstrings(self, s: str) -> str:
        def manacher(s):
            # Preprocessing the string so that all palindromes become odd-length
            # For input string: s = "abba"
            # Transformed string ms: "@#a#b#b#a#$"
            t = '#' + '#'.join(s) + '#'

            # palindromes[i] stores the radius (number of characters on one side) of the 
            # longest palindrome centered at position i
            palindromes = [0] * len(t)

            start, end = 0, 0
            for i in range(len(t)):
                palindromes[i] = 0
                if i < end:
                    palindromes[i] = min(end - i, palindromes[start + (end - i)]) 
                
                while (i + palindromes[i] + 1 < len(t) 
                       and i - palindromes[i] - 1 >= 0
                       and t[i + palindromes[i] + 1] == t[i - palindromes[i] - 1]
                    ):
                    palindromes[i] += 1
                
                if i + palindromes[i] > end:
                    start, end = i - palindromes[i], i + palindromes[i]
            
            return palindromes

        palindromes = manacher(s)
        print(palindromes)
        result = 0
        for index, length in enumerate(palindromes):
            if index % 2 == 1: #length of odd palindrome
                result += math.ceil(length / 2)
            else: #length of even palindrome
                result += math.floor(length / 2)
        return result