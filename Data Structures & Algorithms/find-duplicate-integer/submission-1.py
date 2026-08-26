class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        walk = 0
        while True:
            slow = nums[slow]
            walk = nums[walk]
            if slow == walk:
                return walk