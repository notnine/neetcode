class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = r = 0
        farthest = 0

        while r < len(nums) - 1:
            print("l" + str(l))
            print("r" + str(r))
            print()
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)
            l = r + 1
            r = farthest
            jumps += 1
        
        return jumps
