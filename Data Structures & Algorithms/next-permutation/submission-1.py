class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find the last pair of increasing numbers and flip them, doesn't need to be adj
        # [1,2,3,4,5] -> [1,2,3,5,4]
        # [1,2,5,4,3] -> [1,5,2,4,3]

        a, b = None, None
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    a, b = i, j

        
        if not a and not b:
            # find the 
            nums[0], nums[-1] = nums[-1], nums[0]
        else:
            nums[a], nums[b] = nums[b], nums[a]