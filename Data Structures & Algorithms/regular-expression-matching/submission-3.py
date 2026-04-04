class Solution:
    def isMatch(self, s: str, p: str) -> bool:
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