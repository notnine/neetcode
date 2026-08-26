class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        len_w = len(word)
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        # return True if we can form word from (i,j). k is the pointer to word we are currently checking
        def dfs(i: int, j: int, k: int, visitted: set) -> bool:
            if (board[i][j] == word[k] and k == len_w - 1):
                return True
            
            if (board[i][j] != word[k]):
                return False

            visitted.add((i,j)) # possible path, add (i,j) to visitted

            # for each possible neighbour, return True if we can form the remaining word if we go to that direction
            for d_i, d_j in directions:
                new_i, new_j = i + d_i, j + d_j
                if 0 <= new_i < n and 0 <= new_j < m and (new_i,new_j) not in visitted:
                    if dfs(new_i, new_j, k+1, visitted):
                        return True

            visitted.remove((i,j)) # this path is not valid, backtrack (i,j)
            return False
        
        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0, set()):
                    return True
        
        return False
            