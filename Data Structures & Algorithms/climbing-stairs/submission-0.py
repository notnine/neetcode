class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        dp = [0 for _ in range(n + 1)]

        # dp[i] = # possible steps to i 
        # dp[i] = dp[i-1] + dp[i-2]
        # notice dp[i] only depends on the last 2 elements before it, so we actually only need to store 2 elements before it

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]