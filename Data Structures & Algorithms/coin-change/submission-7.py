class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if min(coins) > amount:
            return -1

        count = 0
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        for coin in coins:
            if coin in range(len(dp)):
                dp[coin] = 1

        for total in range(min(coins), amount + 1):
            possibles = [dp[total - coins[i]] for i in range(len(coins)) if 0 <= (total - coins[i]) <= len(dp)]
            print("total:" + str(total))
            print("possibles")
            print(possibles)
            print()
            dp[total] = 1 + min(
                possibles
            )

        return dp[amount] if dp[amount] != float('inf') else -1