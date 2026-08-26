class Solution:
    def trap(self, height: List[int]) -> int:
        # 2 pointers, moving the limiting height
        # calc the water stored at each index

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l] # if water can sit on top of height at l
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res