class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        n, m = len(text1), len(text2)

        def dfs(i: int, j: int) -> int: # i is a ptr to text1, j to text2
            if i == n or j == m:
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            if text1[i] == text2[j]:
                memo[(i,j)] = 1 + dfs(i+1, j+1)
                return memo[(i,j)]
            
            memo[(i,j)] = max(dfs(i,j+1), dfs(i+1,j))
            return memo[(i,j)]
            
        return dfs(0,0)
                