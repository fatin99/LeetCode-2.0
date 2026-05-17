class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row in matrix:
            for val in row:
                print(val, end=" ")
            print()
        print()

        for row in matrix:
            for val in row:
                print(val, end=" ")
            print()
        print()


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
Solution().setZeroes(matrix)
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
Solution().setZeroes(matrix)
matrix = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
Solution().setZeroes(matrix)
matrix = [[1, 0, 3]]
Solution().setZeroes(matrix)
matrix = [[0, 0, 0, 5], [4, 3, 1, 4], [0, 1, 1, 4], [1, 2, 1, 3], [0, 0, 1, 1]]
Solution().setZeroes(matrix)
