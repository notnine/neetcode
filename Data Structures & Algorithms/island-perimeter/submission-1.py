class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # 1 valid unit of perimeter borders either the border, or water
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        res = 0
        n, m = len(grid), len(grid[0])

        # dfs while counting valid perimeter
        def dfs(i: int, j: int) -> None:
            nonlocal res
            # count the valid perim. borders
            for d_i, d_j in directions:
                new_i, new_j = i + d_i, j + d_j
                # if new pos is out of bounds or new pos is water
                if not ((0 <= new_i < n) and (0 <= new_j < m)) or grid[new_i][new_j] == 0:
                    res += 1

            # recursively call dfs
            for d_i, d_j in directions:
                new_i, new_j = i + d_i, j + d_j
                # if new pos in bounds, land, and not in visited
                if ((0 <= new_i < n) and (0 <= new_j < m)) and grid[new_i][new_j] == 1 and (new_i, new_j) not in visited:
                    visited.add((new_i, new_j))
                    dfs(new_i, new_j)

        
        # find the island, and recurse into it with dfs
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    visited.add((i, j))
                    dfs(i, j)
                    return res