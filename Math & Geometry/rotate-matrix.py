class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        i = 0
        while i <= int(n / 2):
            start = i
            end = n - 1 - i
            count = 0
            length = end - start
            while count < length:
                temp1 = matrix[i][start]
                temp2 = matrix[start][n - 1 - i]
                temp3 = matrix[n - 1 - i][end]
                temp4 = matrix[end][i]
                # print(temp1)
                # print(temp2)
                # print(temp3)
                # print(temp4)

                matrix[start][n - 1 - i] = temp1
                matrix[n - 1 - i][end] = temp2
                matrix[end][i] = temp3
                matrix[i][start] = temp4
                # print(matrix)

                start += 1
                end -= 1
                count += 1
            i += 1

        for row in matrix:
            for val in row:
                print(val, end=" ")
            print()


matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
Solution().rotate(matrix)
