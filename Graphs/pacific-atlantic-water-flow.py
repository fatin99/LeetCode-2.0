from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        hasPath = [
            [[i == 0 or j == 0, i == m - 1 or j == n - 1] for j in range(n)]
            for i in range(m)
        ]
                    
        def bfs(mIndex: int, nIndex: int) -> None:
            queue = deque([(mIndex, nIndex)])

            while queue:
                r, c = queue.popleft()
                visited.add((r,c))

                if r == 0 or c == 0 or hasPath[r][c][0]:
                    hasPath[mIndex][nIndex][0] = True
                if r == m - 1 or c == n - 1 or hasPath[r][c][1]:
                    hasPath[mIndex][nIndex][1] = True

                if all(hasPath[mIndex][nIndex]):
                    return True

                currHeight = heights[r][c]

                # if not hasPath[mIndex][nIndex][0]: #check for path to pacific
                if r > 0 and heights[r - 1][c] <= currHeight and (r - 1, c) not in visited:
                    queue.append((r - 1, c)) #up
                if c > 0 and heights[r][c - 1] <= currHeight and (r, c - 1) not in visited:
                    queue.append((r, c - 1)) #left
                
                # if not hasPath[mIndex][nIndex][1]: #check for path to atlantic
                if r < len(heights) - 1 and heights[r + 1][c] <= currHeight and (r + 1, c) not in visited:
                    queue.append((r + 1, c)) #down
                if c < len(heights[r]) - 1 and heights[r][c + 1] <= currHeight and (r, c + 1) not in visited:
                    queue.append((r, c + 1)) #right
        
            return False
        
        result = []
        for i in range(m):
            for j in range(n):
                if  all(hasPath[i][j]):
                    result.append([i, j])
                else:
                    visited = set()
                    if bfs(i, j):
                        result.append([i, j])

        return result
    
grid = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
]
print(Solution().pacificAtlantic(grid))

grid = [
    [1]
]
print(Solution().pacificAtlantic(grid))

grid = [
    [1,2,3],
    [8,9,4],
    [7,6,5]
]
print(Solution().pacificAtlantic(grid))
