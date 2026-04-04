class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # approach 1: memoized approach 0

        memo = defaultdict(bool)
        len_s, len_p = len(s), len(p)

        # at index i of s, index j of p, return True if isMatch
        def dfs(i: int, j: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i == len_s and j == len_p:
                return True

            # if char after j is *
            if j + 1 < len_p and p[j + 1] == '*':
                take_none = dfs(i, j + 2)
                take_one = False
                if i < len_s and (s[i] == p[j] or p[j] == '.'):
                    take_one = dfs(i + 1, j)
                memo[(i, j)] = take_none or take_one
                return memo[(i, j)]
            
            if (j < len_p and i < len_s) and (p[j] == '.' or s[i] == p[j]):
                if dfs(i+1, j+1):
                    memo[(i, j)] = True
                    return True
            
            memo[(i, j)] = False
            return False
        
        return dfs(0, 0)
            

    def isMatch_approach0(self, s: str, p: str) -> bool:
        # approach 0: brute force

        if not s and not p:
            return True

        # in this uf branch, we can break into 2 branches. so it's O(2^(m+n))
        if len(p) >= 2 and p[1] == '*':
            take_none = self.isMatch(s, p[2:])
            # take 1 if we can
            take_one = False
            if s and (s[0] == p[0] or p[0] == '.'):
                take_one = self.isMatch(s[1:], p)
            return take_none or take_one        
        
        if p and p[0] == '.':
            if not s:
                return False
            else:
                return self.isMatch(s[1:], p[1:])
        
        if p and s and p[0] == s[0]:
            return self.isMatch(s[1:], p[1:])

        return False