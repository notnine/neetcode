class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            # even len where i is "mid point"
            l, r = i, i + 1
            while 0 <= l < len(s) and 0 <= r < len(s) and s[l:r+1] == s[l:r+1][::-1]:
                l, r = l - 1, r + 1
                res += 1

            # odd len where i is mid point
            l, r = i, i
            while 0 <= l < len(s) and 0 <= r < len(s) and s[l:r+1] == s[l:r+1][::-1]:
                l, r = l - 1, r + 1
                res += 1
        
        return res