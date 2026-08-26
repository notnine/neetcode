class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0 # max area so far
        stack = [] # (index, height), non decreasing in height

        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                popped_index, popped_height = stack.pop()
                res = max(res, (index - popped_index) * popped_height)
                start = popped_index
            stack.append((start, height))

        # empty out the stack
        n = len(heights)
        for i, h in stack:
            res = max(res, (n - i) * h)
        
        return res