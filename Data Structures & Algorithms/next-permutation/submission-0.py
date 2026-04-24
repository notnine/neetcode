class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find the last pair of increasing numbers and flip them
        # [1,2,3,4,5] -> [1,2,3,5,4]
        # [1,2,5,4,3] -> [1,5,2,4,3]

        a, b = None, None
        for i in range(0, len(nums) - 1):
            if nums[i] < nums[i+1]:
                a, b = i, i+1
        
        if not a and not b:
            nums[0], nums[-1] = nums[-1], nums[0]
        else:
            nums[i], nums[i+1] = nums[i+1], nums[i]