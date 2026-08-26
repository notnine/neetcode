class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        res, i, j = float('inf'), 0, 0
        dp = {} # stores (i, j, curr)

        # base case: if i is at the end of word1 and len(word2) != len(word1) then return curr + the difference
        def dfs(i: int, j: int, curr: int) -> None:
            nonlocal res

            if (i, j, curr) in dp:
                return dp[(i, j, curr)]

            if i == len(word1):
                res = min(res, curr + len(word2) - j)
                dp[(i, j, curr)] = res
                return
            if j == len(word2):
                res = min(res, curr + len(word1) - i)
                dp[(i, j, curr)] = res
                return

            if word1[i] == word2[j]:
                dfs(i+1, j+1, curr)
            else:
                dfs(i+1, j, curr+1) # insert char at i
                dfs(i, j+1, curr+1) # delete char at i
                dfs(i+1, j+1, curr+1) # replace char at i 

        dfs(0, 0, 0)
        return res