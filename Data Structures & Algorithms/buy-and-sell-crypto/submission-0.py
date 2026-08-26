class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        res = -1

        for price in prices[1:]:
            res = max(res, price - curr_min)
            curr_min = min(curr_min, price)

        return res if res > 0 else 0