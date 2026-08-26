from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs, starting with the chests. at each layer, of bfs traversal, fill pos with min(dist, pos)
        n, m = len(grid), len(grid[0])
        curr_lvl = deque([])
        visited = set()
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    curr_lvl.append((i,j))
                    visited.add((i,j))

        dist = 0

        while curr_lvl:
            next_lvl = deque([])
            while curr_lvl:
                i,j = curr_lvl.popleft()
                grid[i][j] = dist
                neighbours = [(i + dir_i, j + dir_j) for dir_i, dir_j in dirs]
                for nei_i, nei_j in neighbours:
                    if 0 <= nei_i < n and 0 <= nei_j < m and grid[nei_i][nei_j] > 0 and (nei_i, nei_j) not in visited:
                        visited.add((nei_i,nei_j))
                        next_lvl.append((nei_i,nei_j))
            dist+=1
            curr_lvl=next_lvl
        


                
            
            

            


        