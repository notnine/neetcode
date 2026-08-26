class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def dfs(i: int, xor_so_far: int) -> int: # return xor of valid subset
            if i == len(nums): # completed a valid subset. Append to res curr's xor
                return xor_so_far

            return dfs(i+1, xor_so_far ^ nums[i]) + dfs(i+1, xor_so_far) # skip num at i

        return dfs(0, 0)