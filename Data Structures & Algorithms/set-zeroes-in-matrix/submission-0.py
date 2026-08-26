class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        row_got_zero = [False for _ in range(n)]
        col_got_zero = [False for _ in range(m)]

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row_got_zero[i] = True
                    col_got_zero[j] = True
        
        for i in range(n):
            for j in range(m):
                if row_got_zero[i] or col_got_zero[j]:
                    matrix[i][j] = 0
        
