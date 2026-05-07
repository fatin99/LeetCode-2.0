from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        hasPath = [[[False, False] for _ in row] for row in heights]

        def bfs(source, fromPacific) -> None:
            queue = deque(source)
            while queue:
                r, c = queue.popleft()
                ocean = 0 if fromPacific else 1

                hasPath[r][c][ocean] = True
                currHeight = heights[r][c]

                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    newRow = r + dr
                    newCol = c + dc
                    if 0 <= newRow < rows and 0 <= newCol < cols:
                        newHeight = heights[newRow][newCol]

                        newPath = hasPath[newRow][newCol][ocean]
                        if newHeight >= currHeight and not newPath:
                            queue.append((newRow, newCol))

            return

        pacificCells = [(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)]
        atlanticCells = [(r, cols - 1) for r in range(rows)] + [
            (rows - 1, c) for c in range(cols)
        ]

        bfs(pacificCells, True)
        bfs(atlanticCells, False)

        result = []
        for i in range(rows):
            for j in range(cols):
                if all(hasPath[i][j]):
                    result.append([i, j])

        return result


grid = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]
print(Solution().pacificAtlantic(grid))

grid = [[1]]
print(Solution().pacificAtlantic(grid))

grid = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
print(Solution().pacificAtlantic(grid))

grid = [[1, 1], [1, 1], [1, 1]]
print(Solution().pacificAtlantic(grid))
