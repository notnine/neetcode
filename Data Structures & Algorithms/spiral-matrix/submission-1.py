class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])

        # curr row & col borders
        top_row = 0
        bottom_row = ROWS - 1
        left_col = 0
        right_col = COLS - 1

        # curr indices
        i, j = 0, 0

        res = []

        while top_row <= bottom_row and left_col <= right_col:

            # starting at top left, iterate to the right
            while j <= right_col:
                res.append(matrix[i][j])
                j += 1
                print(res)
            j -= 1

            # now go down
            i += 1
            while i <= bottom_row:
                res.append(matrix[i][j])
                i += 1
                print(res)
            i -= 1

            # go left
            j -= 1
            while j >= left_col and bottom_row != top_row:
                res.append(matrix[i][j])
                j -= 1
                print(res)
            j += 1

            # go up
            i -= 1
            while i > top_row and left_col != right_col:
                res.append(matrix[i][j])
                i -= 1
                print(res)
            i += 1

            # update row & col borders
            top_row += 1
            bottom_row -= 1
            left_col += 1
            right_col -= 1

            i, j = top_row, left_col
        
        return res