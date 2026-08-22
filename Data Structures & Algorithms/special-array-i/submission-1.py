class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        for i, num in enumerate(nums):
            curr_even = num % 2 == 0

            if i + 1 < len(nums):
                next_even = nums[i+1] % 2 == 0
                if (not curr_even and next_even) or (curr_even and not next_even):
                    continue
                else:
                    return False
        
        return True