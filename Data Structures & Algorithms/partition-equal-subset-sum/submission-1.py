class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2 # find a subset where sum is target
        n = len(nums)
        memo = {} # stores (i,curr) to bool if possible

        def dfs(i: int, curr: int) -> bool:
            nonlocal target
            nonlocal n
            if (i, curr) in memo:
                return memo[(i, curr)]
            if curr == target:
                memo[(i, curr)] = True
                return True
            if i == n or curr > target:
                memo[(i, curr)] = False
                return False
            # take num at i or skip num at i
            return dfs(i+1, curr + nums[i]) or dfs(i+1, curr)

        return dfs(0, 0)
