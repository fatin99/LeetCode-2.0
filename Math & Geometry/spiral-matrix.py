class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        i = 0
        j = 0

        res = []

        while i < n/2 and j < m/2:
            count = 0
            while count < 4:
                if count % 2 == 0:
                    for k in range(j, m - j):
                        if count == 0:
                            res.append(matrix[j][k])
                        elif count == 2:
                            if k == j or (i == int(n/2) and n%2 == 1):
                                continue
                            res.append(matrix[-1-j][-1-k])
                else:
                    for k in range(i, n - i):
                        if count == 1:
                            if k == i:
                                continue
                            res.append(matrix[k][-1-i])
                        elif count == 3:
                            if k == i or k == n-i-1 or (j == int(m/2) and m%2 == 1):
                                continue
                            res.append(matrix[-1-k][i])

                count += 1
            i += 1
            j += 1
        
        return res
    
    def spiralOrder(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        res = []

        top = 0
        bottom = n - 1
        left = 0
        right = m - 1

        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            for row in range(top + 1, bottom + 1):
                res.append(matrix[row][right])
                
            if top != bottom:
                for col in range(right - 1, left - 1, -1):
                    res.append(matrix[bottom][col])
            if left != right:
                for row in range(bottom - 1, top, -1):
                    res.append(matrix[row][left])

            top += 1
            bottom -= 1
            left += 1
            right -= 1

        return res
                    
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()
print(Solution().spiralOrder(matrix))
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()
print(Solution().spiralOrder(matrix))
matrix = [[2,5,8],[4,0,-1]]
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()
print(Solution().spiralOrder(matrix))
