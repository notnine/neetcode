class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {} # stores (i,j) -> bool
        n, m = len(s1), len(s2)

        def dfs(i: int, j: int) -> bool:
            if i == n and j == m and i + j == len(s3):
                return True
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            if i < n and i+j < len(s3) and s1[i] == s3[i+j] and dfs(i+1, j):
                return True
            if j < m and i+j < len(s3) and s2[j] == s3[i+j] and dfs(i, j+1):
                return True
            
            dp[(i,j)] = False
            return False
        
        return dfs(0,0)