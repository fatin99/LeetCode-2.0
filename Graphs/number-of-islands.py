class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(mIndex: int, nIndex: int) -> None:
            if grid[mIndex][nIndex] == "0":
                return
            else: #grid[mIndex][nIndex] == 1
                grid[mIndex][nIndex] = "0"
            
            if mIndex > 0:
                dfs(mIndex - 1, nIndex)
            if nIndex > 0:
                dfs(mIndex, nIndex- 1)
            if mIndex < len(grid) - 1:
                dfs(mIndex + 1, nIndex)
            if nIndex < len(grid[mIndex]) - 1:
                dfs(mIndex, nIndex + 1)
            return

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)

        return islands
    
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(Solution().numIslands(grid))