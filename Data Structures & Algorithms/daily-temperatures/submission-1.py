class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # contains (i, temp), nondecreasing in temp
        res = [0 for _ in range(len(temperatures))]

        for i, t in enumerate(temperatures):            
            while stack and t > stack[-1][1]:
                popped_i, popped_t = stack.pop()
                res[popped_i] = i - popped_i
            stack.append((i, t))

        return res
