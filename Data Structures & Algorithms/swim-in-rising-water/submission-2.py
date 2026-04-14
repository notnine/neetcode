class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # graph traversal with relaxation
        # relax neighbors, traverse to nei only if we found a cheaper way to nei


        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        ROWS, COLS = len(grid), len(grid[0])
        cost = [[float('inf') for c in range(COLS)] for r in range(ROWS)] # best cost to reach pos (r,c) so far
        cost[0][0] = grid[0][0]

        def relax(r: int, c: int) -> None:
            neighbors_to_process = []
            for d_r, d_c in directions:
                n_r, n_c = r + d_r, c + d_c
                if 0 <= n_r < ROWS and 0 <= n_c < COLS and cost[n_r][n_c] > max(grid[n_r][n_c], cost[r][c]):
                    cost[n_r][n_c] = max(grid[n_r][n_c], cost[r][c])
                    neighbors_to_process.append((n_r, n_c))
                    
            for n_r, n_c in neighbors_to_process:
                relax(n_r, n_c)

        relax(0,0)
        return cost[ROWS - 1][COLS - 1]
