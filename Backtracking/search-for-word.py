class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(strIndex: int, mIndex: int, nIndex: int) -> None:
            if (mIndex, nIndex) in visited:
                return
            
            if not board[mIndex][nIndex] == word[strIndex]:
                return
            board[mIndex][nIndex] = "#"
            strIndex += 1
            if strIndex == len(word):
                return True
            
            if mIndex > 0:
                if dfs(strIndex, mIndex - 1, nIndex):
                    return True
            if nIndex > 0:
                if dfs(strIndex, mIndex, nIndex- 1):
                    return True
            if mIndex < len(board) - 1:
                if dfs(strIndex, mIndex + 1, nIndex):
                    return True
            if nIndex < len(board[mIndex]) - 1:
                if dfs(strIndex, mIndex, nIndex + 1):
                    return True
            board[mIndex][nIndex] = word[strIndex - 1]
            return
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(0, i, j):
                    return True
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:        
        for i in range(len(board)):
            for j in range(len(board[i])):
                stack = [(0, i, j, set())]
                while stack:
                    strIndex, mIndex, nIndex, visited = stack.pop()
                    if (mIndex, nIndex) in visited:
                        continue
                    
                    if not board[mIndex][nIndex] == word[strIndex]:
                        continue
                    strIndex += 1
                    if strIndex == len(word):
                        return True

                    if mIndex > 0:
                        stack.append((strIndex, mIndex - 1, nIndex, visited | {(mIndex, nIndex)}))
                    if nIndex > 0:
                        stack.append((strIndex, mIndex, nIndex- 1, visited | {(mIndex, nIndex)}))
                    if mIndex < len(board) - 1:
                        stack.append((strIndex, mIndex + 1, nIndex, visited | {(mIndex, nIndex)}))
                    if nIndex < len(board[mIndex]) - 1:
                        stack.append((strIndex, mIndex, nIndex + 1, visited | {(mIndex, nIndex)}))
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
