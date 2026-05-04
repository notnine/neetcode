class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        res = 0

        for i, h in enumerate(heights):
            if heights[i] != sorted_heights[i]:
                res += 1
        
        return res