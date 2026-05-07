class Solution:
    paths = {}

    # Iterative
    def uniquePaths(self, m: int, n: int) -> int:
        for i in range(m):
            self.paths[(i, 0)] = 1
        for j in range(n):
            self.paths[(0, j)] = 1

        for row in range(1, m):
            for col in range(1, n):
                self.paths[(row, col)] = (
                    self.paths[(row - 1, col)] + self.paths[(row, col - 1)]
                )

        return self.paths[(m - 1, n - 1)]

    # Recursive
    def uniquePaths(self, m: int, n: int) -> int:
        for i in range(m):
            self.paths[(i, 0)] = 1
        for j in range(n):
            self.paths[(0, j)] = 1

        def move(row, col):
            if (row, col) in self.paths:
                return self.paths[(row, col)]
            self.paths[(row, col)] = move(row - 1, col) + move(row, col - 1)
            return self.paths[(row, col)]

        return move(m - 1, n - 1)


print(Solution().uniquePaths(3, 2))
print(Solution().uniquePaths(3, 7))
