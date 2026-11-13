class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        t, b = 0, len(matrix) - 1

        # [1,2,3]
        # [4,5,6]
        # [7,8,9]

        while l < r:
            for i in range(r-l):
                # move top left to top right
                top_right = matrix[t+i][r]
                matrix[t+i][r] = matrix[t][l+i]

                # move top right to bottom right
                bottom_right = matrix[b][r-i]
                matrix[b][r-i] = top_right

                # move bottom right to bottom left
                bottom_left = matrix[b-i][l]
                matrix[b-i][l] = bottom_right

                # move bottom left to top left
                matrix[t][l+i] = bottom_left
            
            l, r = l+1, r-1
            t, b = t+1, b-1