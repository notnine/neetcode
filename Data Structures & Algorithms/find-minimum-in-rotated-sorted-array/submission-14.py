class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if r-l <= 2:
                return min(nums[l], nums[m], nums[r])
            elif nums[m] > nums[r]: # unsorted is right side
                l = m + 1
            else:
                r = m
            
        return nums[l]