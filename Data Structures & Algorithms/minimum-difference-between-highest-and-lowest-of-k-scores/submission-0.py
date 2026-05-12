class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # n log n time

        nums.sort()
        r = k - 1
        res = float('inf')
        n = len(nums)

        while r < n:
            l = r - k + 1
            diff = nums[r] - nums[l]
            res = min(res, diff)
            r += 1

        return res
