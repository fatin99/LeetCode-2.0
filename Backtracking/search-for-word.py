class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(currStr: int, mIndex: int, nIndex: int, visited: set) -> None:
            char = board[mIndex][nIndex]
            newStr = currStr + char
            if not word.startswith(newStr):
                return
            if (mIndex, nIndex) in visited:
                return
            if newStr == word:
                return True
            
            if mIndex > 0:
                if dfs(newStr, mIndex - 1, nIndex, visited | {(mIndex, nIndex)}):
                    return True
            if nIndex > 0:
                if dfs(newStr, mIndex, nIndex- 1, visited | {(mIndex, nIndex)}):
                    return True
            if mIndex < len(board) - 1:
                if dfs(newStr, mIndex + 1, nIndex, visited | {(mIndex, nIndex)}):
                    return True
            if nIndex < len(board[mIndex]) - 1:
                if dfs(newStr, mIndex, nIndex + 1, visited | {(mIndex, nIndex)}):
                    return True
            return
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs("", i, j, set()):
                    return True
        return False
        
# A B C E
# S F C S
# A D E E
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(Solution().exist(board, word))

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
print(Solution().exist(board, word))

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(Solution().exist(board, word))

    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     res = []

    #     def dfs(currSum: int, currNums: List[int], index: int) -> None:
    #         if currSum == target:
    #             res.append(list(currNums))
    #             return
    #         while index < len(candidates):
    #             num = candidates[index]
    #             newSum = currSum + num
    #             if newSum > target:
    #                 index += 1
    #                 continue
    #             currNums.append(num)
    #             dfs(newSum, currNums, index)
    #             currNums.pop()
    #             index += 1

    #     dfs(0, [], 0)
    #     return res
