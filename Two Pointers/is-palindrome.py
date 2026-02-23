class Solution:
    def isPalindrome(self, s: str) -> bool:
        # char is left pointer, back is right pointer
        back = len(s) - 1
        for char in s:
            if not char.isalnum():
                continue
            while not s[back].isalnum():
                back -= 1
            # print(f"Comparing {char.lower()} and {s[back].lower()}")
            if char.lower() == s[back].lower():
                back -= 1
                continue
            else:
                return False
        return True

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
