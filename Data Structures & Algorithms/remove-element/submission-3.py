class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1
        k = 0

        while l <= r:
            print(nums)
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
                k += 1
                # num at l might still be val
            else:
                l += 1
            
        return len(nums) - k
