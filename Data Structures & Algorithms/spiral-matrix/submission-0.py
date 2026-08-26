class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        right, down, left, up = (0,1), (1,0), (0,-1), (-1,0)
        t_border, b_border, l_border, r_border = 0, len(matrix) - 1, 0, len(matrix[0]) - 1 # valid coords of border
        traversed, total = 0, len(matrix) * len(matrix[0])
        res = []

        while (b_border - t_border) >= 0: # while at least 1 row
            # peel layer off
            i, j = t_border, l_border # top left of current layer

            # go right
            for curr_j in range(j, r_border + 1):
                traversed += 1
                res.append(matrix[i][curr_j])
                if traversed == total:
                    return res

            i, j = t_border + 1, r_border # top right (but 1 down)
            # go down
            for curr_i in range(i, b_border + 1):
                traversed += 1
                res.append(matrix[curr_i][j])
                if traversed == total:
                    return res

            i, j = b_border, r_border - 1 # bottom right (but 1 left)
            # go left
            for curr_j in range(j, l_border - 1, -1): # and skip top left
                traversed += 1
                res.append(matrix[i][curr_j])
                if traversed == total:
                    return res

            i, j = b_border - 1, l_border # bottom left (but 1 up)
            # go up        
            for curr_i in range(i, t_border, -1):
                traversed += 1
                res.append(matrix[curr_i][curr_j])
                if traversed == total:
                    return res

            # shrink border
            t_border += 1
            b_border -= 1
            l_border += 1
            r_border -= 1
        
        return res

[1,2,3,4]
[5,6,7,8]
[9,10,11,12]