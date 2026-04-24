class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # sliding window approach, O(n) time

        zeroes = 0
        l, r = 0, 0
        res = 0

        while r < len(nums):
            if nums[r] == 0:
                zeroes += 1

            while zeroes > k and l <= r:
                if nums[l] == 0:
                    zeroes -= 1
                l += 1
            

            res = max(res, r - l + 1)
            r += 1
        
        return res