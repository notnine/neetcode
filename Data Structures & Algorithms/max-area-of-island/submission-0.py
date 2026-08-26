class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visitted = set() # island coords that's been visited
        res = 0 # max island area so far
        directions = [(-1,0), (0,-1), (1,0), (0,1)]
        rows, cols = len(grid), len(grid[0])

        # x, y is an unvisited island position
        def visit_island(x: int, y: int) -> None:
            visitted.add((x,y))
            for d in directions:
                new_x, new_y = x + d[0], y + d[1]
                if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == 1 and (new_x, new_y) not in visitted:
                    visit_island(new_x, new_y)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row,col) not in visitted:
                    before = len(visitted)
                    visit_island(row, col)
                    after = len(visitted)
                    res = max(res, after - before)

        return res
