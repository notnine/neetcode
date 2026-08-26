class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l, r = 0, rows * cols - 1
        m = (l + r) // 2

        while l <= r:
            row_index = m // cols
            col_index = m % cols
            curr = matrix[row_index][col_index]
            if curr < target:
                l = m + 1
            elif curr > target:
                r = m - 1
            else:
                return True
            m = (l + r) // 2
        
        return False