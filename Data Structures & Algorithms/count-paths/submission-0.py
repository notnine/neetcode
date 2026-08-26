class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] denotes the number of ways to get to position i,j
        # dp[i][j] = num of ways from the left tile + num of ways from above tile = dp[i][j-1] + dp[i-1][j]

        dp = []
        for row in range(m):
            dp.append([0 for _ in range(n)])

        # notice tiles in first row & first col there's only 1 way to get to these
        for i in range(m):
            for j in range(n):
                if i == 0: # if first row
                    dp[0][j] = 1
                elif j == 0: # first col
                    dp[i][0] = 1
        
        # calculate every other tile
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return dp[m-1][n-1]
        