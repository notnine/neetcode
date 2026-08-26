# class Solution:
#     def stoneGameIII(self, stoneValue: List[int]) -> str:
#         n = len(stoneValue)
#         memo = {}

#         def dp(i: int) -> int:
#             if i >= n:
#                 return 0
#             if i in memo:
#                 return memo[i]
            
#             best = -float('inf')
#             take = 0
#             for k in range(3):
#                 if i + k < n:
#                     take += stoneValue[i + k]
#                     best = max(best, take - dp(i + k + 1))
#             memo[i] = best
#             return best
        
#         res = dp(0)
#         if res < 0:
#             return 'Bob'
#         elif res > 0:
#             return 'Alice'
#         else:
#             return 'Tie'

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [float("-inf")] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            total = 0
            for j in range(i, min(i + 3, n)):
                total += stoneValue[j]
                dp[i] = max(dp[i], total - dp[j + 1])

        result = dp[0]
        if result == 0:
            return "Tie"
        return "Alice" if result > 0 else "Bob"