class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]

        t, b, l, r = 0, n - 1, 0, n - 1
        i, j = 0, 0
        num = 1

        while t <= b:
            
            # fill out the curr top row
            while j <= r:
                res[i][j] = num
                j += 1
                num += 1
            j -= 1
            
            # fill out the curr right col
            i += 1
            while i <= b:
                res[i][j] = num
                i += 1
                num += 1
            i -= 1

            # fill out the curr bottom row
            j -= 1
            while j >= l:
                res[i][j] = num
                j -= 1
                num += 1
            j += 1

            # fill out the left col
            i -= 1
            while i > t:
                res[i][j] = num
                i -= 1
                num += 1
            i += 1
            
            t, b, l, r = t + 1, b - 1, l + 1, r - 1
            i, j = t, l

        return res
