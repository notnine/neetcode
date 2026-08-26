class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(1,0), (-1,0),(0,1),(0,-1)]
        res = 0
        
        def sink(row: int, col: int) -> None:
            grid[row][col] = "0"
            new_poses = [(row + i, col + j) for (i, j) in dirs]
            for i, j in new_poses:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
                    sink(i, j)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    res += 1
                    sink(row, col)

        return res
        