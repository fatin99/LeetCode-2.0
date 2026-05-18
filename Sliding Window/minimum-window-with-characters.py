from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        if len(t) > len(s) or len(s) == 0:
            return res
        char_map = {}
        for char in t:
            if char in char_map:
                char_map[char] += 1
            else:
                char_map[char] = 1

        start = 0
        for end in range(1, len(s) + 1):
            newChar = s[end - 1]
            if newChar in char_map:
                char_map[newChar] -= 1
                if char_map[newChar] <= 0:  # reduce size of window
                    while (
                        all(value <= 0 for value in char_map.values())
                        or s[start] not in char_map
                    ):
                        if s[start] in char_map:
                            if char_map[s[start]] < 0:
                                char_map[s[start]] += 1
                            else:
                                break
                        start += 1
            
            if all(value <= 0 for value in char_map.values()):
                if res == "" or end-start < len(res):
                    res = s[start:end]
        return res


s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow(s, t))
s = "ab"
t = "b"
print(Solution().minWindow(s, t))
s = "bbaa"
t = "aba"
print(Solution().minWindow(s, t))
