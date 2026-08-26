class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}

        def dfs(i: int, balance: int) -> int:
            nonlocal n
            if (i, balance) in memo:
                return memo[(i, balance)]
            if i == n - 1:
                res = 0
                if (balance + nums[n - 1]) == target:
                    res += 1
                if (balance - nums[n - 1]) == target:
                    res += 1
                memo[(i, balance)] = res
                return memo[(i, balance)]

            memo[(i, balance)] = dfs(i+1, balance + nums[i]) + dfs(i+1, balance - nums[i])
            return memo[(i, balance)]
        
        return dfs(0, 0)