class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def dfs(i: int, xor_so_far: int) -> None:
            nonlocal res

            if i == len(nums): # completed a valid subset. Append to res curr's xor
                res += xor_so_far
                return

            dfs(i+1, xor_so_far ^ nums[i]) # take num at i
            dfs(i+1, xor_so_far) # skip num at i

        dfs(0, 0)
        return res