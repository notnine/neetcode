class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {} # stores (i, j)

        def dfs(i: int, j: int) -> int:
            if (i, j) in dp:
                return dp[(i, j)]

            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i+1, j+1)
            else:
                insert = 1 + dfs(i+1, j) # insert char at i
                delete = 1 + dfs(i, j+1) # delete char at i
                replace = 1 + dfs(i+1, j+1) # replace char at i
                dp[(i, j)] = min(insert, delete, replace)

            return dp[(i, j)]
        
        return dfs(0, 0)