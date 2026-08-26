class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}
        # memo[(i, holding)] holds the sub solution for the max profit we can achieve starting at day i, with holding state holding

        # when holding is True, we are holding a stock. 
            # we can either sell, or nothing
        # when holding is False, we are not holding a stock.
            # we can either buy, or nothing

        def dfs(i: int, holding: bool) -> int:
            if i >= n:
                return 0
            if (i, holding) in memo:
                return memo[(i, holding)]

            if holding:
                sell = prices[i] + dfs(i+2, False)
                nothing = dfs(i+1, True)
                memo[(i, holding)] = max(sell, nothing)
            else:
                buy = -prices[i] + dfs(i+1, True)
                nothing = dfs(i+1, False)
                memo[(i, holding)] = max(buy, nothing)

            return memo[(i, holding)]


        return dfs(0, False)
        