class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(i: int, j: int) -> None:
            for d_i, d_j in directions:
                new_i, new_j = i + d_i, j + d_j
                if 0 <= new_i < n and 0 <= new_j < m and board[new_i][new_j] == "O":
                    board[new_i][new_j] = "#"
                    dfs(new_i, new_j)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and (i == 0 or i == n - 1 or j == 0 or j == m - 1):
                    board[i][j] = "#"
                    dfs(i, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"

        for i in range(n):
            for j in range(m):
                if board[i][j] == "#":
                    board[i][j] = "O"