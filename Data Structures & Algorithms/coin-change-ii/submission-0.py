class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = 0
        n = len(coins)
        memo = {}

        def dfs(i: int, balance: int) -> int:
            nonlocal res

            if (i, balance) in memo:
                return memo[(i, balance)]

            if balance == amount:
                return 1

            if i >= n or balance > amount:
                return 0

            memo[(i, balance)] = dfs(i, balance + coins[i]) + dfs(i+1, balance) # num ways when take coin + skip coin
            return memo[(i, balance)]

        return dfs(0, 0)
