class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        without_first = self.houseRobberOne(nums[1:])
        without_last = self.houseRobberOne(nums[:len(nums)-1])
        return max(without_first, without_last)
        
    def houseRobberOne(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0

        for n in nums:
            newRob = max(prev2 + n, prev1)
            prev2 = prev1
            prev1 = newRob
        
        return prev1