class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        n, m = len(word1), len(word2)
        res = ''

        while i < n and j < m:
            res += word1[i]
            res += word2[j]
            i, j = i + 1, j + 1
        
        if i != n: # we have not finished off word1
            res += word1[i:]
        elif j != m:
            res += word2[j:]
        
        return res