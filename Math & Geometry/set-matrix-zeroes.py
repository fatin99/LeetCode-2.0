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

        n = len(matrix)
        m = len(matrix[0])

        row0_zero = any(matrix[0][i] == 0 for i in range(m))
        col0_zero = any(matrix[i][0] == 0 for i in range(n))

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0            
        
        for i in range(n):
            if matrix[i][0] == 0 and i >= 1:
                for j in range(1, m):
                    matrix[i][j] = 0
            if col0_zero:
                matrix[i][0] = 0

        for j in range(m):
            if matrix[0][j] == 0 and j >= 1:
                for i in range(1, n):
                    matrix[i][j] = 0
            if row0_zero:
                matrix[0][j] = 0

        for row in matrix:
            for val in row:
                print(val, end=" ")
            print()
        print()


# matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Solution().setZeroes(matrix)
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Solution().setZeroes(matrix)
# matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
# Solution().setZeroes(matrix)
# matrix = [[1, 0, 3]]
# Solution().setZeroes(matrix)
# matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
# Solution().setZeroes(matrix)
