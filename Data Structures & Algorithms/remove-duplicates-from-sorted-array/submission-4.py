class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = nums[0]
        overwriter = 0 # overwritig index
        checker = 0

        while checker < len(nums):
            if nums[checker] == curr:
                checker += 1
            else:
                nums[overwriter] = curr
                curr = nums[checker]
                overwriter += 1

        # last one
        nums[overwriter] = curr
        
        return overwriter + 1