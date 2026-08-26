from collections import deque

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = deque(nums)
        for i in range(k):
            popped = res.pop()
            res.appendleft(popped)
        
        for i in range(len(nums)):
            nums[i] = res[i]