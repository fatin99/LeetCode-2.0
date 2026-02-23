class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # charPrimes = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101}

        # groups = {}
        # for string in strs:
        #     charPrime = 1
        #     for char in string:
        #         charPrime *= charPrimes[char]
        #     if charPrime in groups:
        #         groups[charPrime].append(string)
        #     else:
        #         groups[charPrime] = [string]
        
        # anagrams = []
        # for group, strings in groups.items():
        #     anagrams.append(strings)
        # return anagrams
    
    # We can simply use an array of size O(26), since the character set is a through z 
    # (26 continuous characters), to count the frequency of each character in a string. 
    # Then, we can use this array as the key in the hash map to group the strings. 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            chars = [0] * 26
            for char in string:
                chars[ord(char) - 97] += 1
            chars = ''.join(str(chars))
            if chars in groups:
                groups[chars].append(string)
            else:
                groups[chars] = [string]
        
        anagrams = []
        for group, strings in groups.items():
            anagrams.append(strings)
        return anagrams
    

    
import math

# def is_prime(n):
#     """Check if a number is prime using trial division up to the square root."""
#     if n <= 1:
#         return False
#     # Check for factors from 2 up to the square root of n
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True

# def get_primes_in_range(start, end):
#     """Generate a list of all prime numbers within a specified range."""
#     primes = []
#     count = 26
#     num = 0
#     while count > 0:
#         if is_prime(num):
#             primes.append(num)
#             count -= 1 
#         num += 1
#     return primes

# primes = get_primes_in_range(0, 1000)
# charPrimes = {}
# char = 'a'
# for prime in primes:
#     charPrimes[char] = prime
#     char = chr(ord(char) + 1)
# print(charPrimes)
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

        
#Input: strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

#replace each char with a prime number and multiply to represent str