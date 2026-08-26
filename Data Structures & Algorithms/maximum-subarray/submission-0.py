class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        res = 0
        above_zero = False
        largest = -float('inf')
        
        for num in nums:
            largest = max(largest, num)
            if num > 0:
                above_zero = True
            curr += num
            if curr < 0: curr = 0
            res = max(res, curr)
        
        if not above_zero:
            return largest
        
        return res
        