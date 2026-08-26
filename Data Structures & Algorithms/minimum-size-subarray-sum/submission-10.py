class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        res = float('inf')
        l, r = 0, 0 # window is l to r inclusive
        curr = 0

        while r < len(nums):
            curr += nums[r]
            r += 1

            while curr >= target: # update res, decrease window
                res = min(res, r - l)
                curr -= nums[l]
                l += 1
        
        return res if res != float('inf') else 0