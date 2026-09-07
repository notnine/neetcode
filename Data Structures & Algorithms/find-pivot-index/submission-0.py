class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left = sum(nums)

        running_sum = 0
        for i in range(n):
            if running_sum == left - nums[i]:
                return i
            running_sum += nums[i]
            left -= nums[i]
        
        return -1
