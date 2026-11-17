class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # overwrite the matrix so each coord is the max height of a col with this pos as its bottom
        ROWS, COLS = len(matrix), len(matrix[0])
        for r in range(1, ROWS):
            for c in range(COLS):
                if matrix[r][c] == 1:
                    matrix[r][c] += matrix[r-1][c]
        
        # for each row, greedily calc the max area of a rectangle as if this were its bottom right
        res = 0
        for row in matrix:
            sorted_row = sorted(row, reverse=True)
            for i in range(COLS):
                curr = (1 + i) * sorted_row[i]
                res = max(res, curr)
        
        return res
