class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res = [-1, -1]
        n = len(grid)
        nums = set()

        for num in range(n*n):
            nums.add(num+1)
        
        for r in range(n):
            for c in range(n):
                num = grid[r][c]
                if num in nums:
                    nums.remove(num)
                else: # num is A
                    res[0] = num

        # the final num in the set is B
        res[1] = nums.pop() # since we are guaranteed to have 1 item here, we can safely pop from the set

        return res
