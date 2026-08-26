class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0 # farthest reachable index so far
        i = 0

        # while i is not last index, and we can reach i
        while i < len(nums) - 1 and farthest >= i:
            farthest = max(farthest, i + nums[i])
            i += 1

        return farthest >= len(nums) - 1