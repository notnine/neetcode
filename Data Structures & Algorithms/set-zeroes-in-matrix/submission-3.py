class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        row_zero = False
        col_zero = False

        for num in matrix[0]: # for num in first row
            if num == 0:
                row_zero = True

        for row in matrix: # for first num of each row (for num in first col)
            if row[0] == 0:
                col_zero = True
            
        for r in range(1, n):
            for c in range(1, m):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        for r in range(1, n):
            for c in range(1, m):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if row_zero:
            for i in range(m):
                matrix[0][i] = 0

        if col_zero:
            for i in range(n):
                matrix[i][0] = 0
