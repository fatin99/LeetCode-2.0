class Solution:
    def match(self, open, close):
        return (
            (open == "(" and close == ")")
            or (open == "[" and close == "]")
            or (open == "{" and close == "}")
        )

    def isValid(self, s: str) -> bool:
        open = []  # this is a stack
        for bracket in s:
            if bracket in ["(", "[", "{"]:
                open.append(bracket)
            if bracket in [")", "]", "}"]:
                if len(open) == 0:  # alternatively: if open
                    return False
                if self.match(open[-1], bracket):
                    open.pop()
                else:
                    return False
        if len(open) > 0:
            return False
        return True


print(Solution().maxProfit([7, 1, 5, 0, 6, 4]))
