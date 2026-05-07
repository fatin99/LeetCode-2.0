from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # https://docs.python.org/2/library/stdtypes.html#dict.get
        # s_map = {}
        # for char in s:
        #     s_map[char] = s_map.get(char, 0) + 1
        # t_map = {}
        # for char in t:
        #     t_map[char] = t_map.get(char, 0) + 1
        # return s_map == t_map

        # https://docs.python.org/3/library/collections.html#collections.Counter
        return Counter(s) == Counter(t)
