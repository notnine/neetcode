class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] = min cost to reach step i where i is index at cost
        # recursion relation: dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        n = len(cost)
        dp = [float('inf') for _ in range(n + 1)] # return dp[n]
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[n]
