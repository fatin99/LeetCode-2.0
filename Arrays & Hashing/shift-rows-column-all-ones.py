# Time:  O(rows * cols^2) — for each of rows*cols target cells, scan up to cols ones
# Space: O(rows * cols) — cost matrix (ones list per row is reused, O(cols))
class Solution:
    def minShifts(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        cost = [[0] * cols for _ in range(rows)]

        # For each row, collect positions of 1s.
        for i in range(rows):
            ones = []
            for c in range(cols):
                if matrix[i][c] == 1:
                    ones.append(c)
            # If a row has none, return -1.
            if not ones:
                return -1

            for j in range(cols):
                best = cols
                for target in ones:
                    # cyclic distance from any 1 in current row to column j (left shift and right shift)
                    left = (target - j) % cols
                    right = (j - target) % cols

                    dist = min(left, right)
                    best = min(best, dist)

                cost[i][j] = best

        # minimize the sum of per-row costs.
        res = -1
        for j in range(cols):
            total = 0
            for i in range(rows):
                total += cost[i][j]
            if res == -1:
                res = total
            res = min(res, total)
        return res


# Already aligned — column 0 is all 1s, no shifts needed. Expect 0.
matrix1 = [
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
]
print(Solution().minShifts(matrix1))

# Identity diagonal — every column needs 2 total shifts. Expect 2.
matrix2 = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
]
print(Solution().minShifts(matrix2))

# Multiple 1s per row — pick whichever 1 is closest. Expect 1.
matrix3 = [
    [1, 0, 1, 0],
    [0, 1, 0, 1],
]
print(Solution().minShifts(matrix3))

# Row of all zeros — impossible. Expect -1.
matrix4 = [
    [1, 0],
    [0, 0],
]
print(Solution().minShifts(matrix4))

# Single column, all 1s — trivially aligned. Expect 0.
matrix5 = [
    [1],
    [1],
    [1],
]
print(Solution().minShifts(matrix5))

# Larger 5x6 — mixed densities, multiple 1s per row, cyclic shortcut matters.
# Best column is 0 (sum of per-row min cyclic distances = 0+1+3+0+1). Expect 5.
matrix6 = [
    [1, 0, 0, 0, 1, 0],  # ones at 0, 4 -> col 0 cost 0
    [0, 1, 0, 0, 0, 0],  # one  at 1   -> col 0 cost 1
    [0, 0, 0, 1, 0, 0],  # one  at 3   -> col 0 cost 3
    [1, 0, 1, 0, 0, 0],  # ones at 0, 2 -> col 0 cost 0
    [0, 0, 0, 0, 0, 1],  # one  at 5   -> col 0 cost 1 (wraps right)
]
print(Solution().minShifts(matrix6))
