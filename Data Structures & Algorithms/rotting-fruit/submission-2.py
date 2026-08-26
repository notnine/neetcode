from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, fresh = -1, 0
        curr_lvl = deque([])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    curr_lvl.append((i,j))

        if fresh == 0:
            return 0
        
        while curr_lvl:
            time += 1
            next_lvl = []
            while curr_lvl:
                curr_i, curr_j = curr_lvl.popleft()
                for d_i, d_j in directions:
                    new_i, new_j = curr_i + d_i, curr_j + d_j
                    if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 0
                        fresh -= 1
                        next_lvl.append((new_i, new_j))
            curr_lvl = deque(next_lvl)

        return time if fresh == 0 else -1
