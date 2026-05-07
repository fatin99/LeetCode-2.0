from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(mIndex: int, nIndex: int) -> None:
            if grid[mIndex][nIndex] == "0":
                return
            else:  # grid[mIndex][nIndex] == 1
                grid[mIndex][nIndex] = "0"

            if mIndex > 0:
                dfs(mIndex - 1, nIndex)
            if nIndex > 0:
                dfs(mIndex, nIndex - 1)
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

    # DFS Iterative
    def numIslands4(self, grid: List[List[str]]) -> int:

        def dfs(mIndex: int, nIndex: int) -> None:
            stack = [(mIndex, nIndex)]
            grid[mIndex][nIndex] = "0"
            while stack:
                r, c = stack.pop()
                if r > 0 and grid[r - 1][c] == "1":
                    grid[r - 1][c] = "0"
                    stack.append((r - 1, c))
                if c > 0 and grid[r][c - 1] == "1":
                    grid[r][c - 1] = "0"
                    stack.append((r, c - 1))
                if r < len(grid) - 1 and grid[r + 1][c] == "1":
                    grid[r + 1][c] = "0"
                    stack.append((r + 1, c))
                if c < len(grid[r]) - 1 and grid[r][c + 1] == "1":
                    grid[r][c + 1] = "0"
                    stack.append((r, c + 1))

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)

        return islands

    # BFS Iterative
    def numIslands2(self, grid: List[List[str]]) -> int:

        def bfs(mIndex: int, nIndex: int) -> None:
            queue = deque([(mIndex, nIndex)])
            grid[mIndex][nIndex] = "0"
            while queue:
                r, c = queue.popleft()
                if r > 0 and grid[r - 1][c] == "1":
                    grid[r - 1][c] = "0"
                    queue.append((r - 1, c))
                if c > 0 and grid[r][c - 1] == "1":
                    grid[r][c - 1] = "0"
                    queue.append((r, c - 1))
                if r < len(grid) - 1 and grid[r + 1][c] == "1":
                    grid[r + 1][c] = "0"
                    queue.append((r + 1, c))
                if c < len(grid[r]) - 1 and grid[r][c + 1] == "1":
                    grid[r][c + 1] = "0"
                    queue.append((r, c + 1))

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    islands += 1
                    bfs(i, j)

        return islands

    # BFS Recursive
    def numIslands3(self, grid: List[List[str]]) -> int:

        def bfs(queue: deque) -> None:
            if not queue:
                return
            r, c = queue.popleft()
            if r > 0 and grid[r - 1][c] == "1":
                grid[r - 1][c] = "0"
                queue.append((r - 1, c))
            if c > 0 and grid[r][c - 1] == "1":
                grid[r][c - 1] = "0"
                queue.append((r, c - 1))
            if r < len(grid) - 1 and grid[r + 1][c] == "1":
                grid[r + 1][c] = "0"
                queue.append((r + 1, c))
            if c < len(grid[r]) - 1 and grid[r][c + 1] == "1":
                grid[r][c + 1] = "0"
                queue.append((r, c + 1))
            bfs(queue)

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    islands += 1
                    grid[i][j] = "0"
                    bfs(deque([(i, j)]))

        return islands


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print(Solution().numIslands(grid))
