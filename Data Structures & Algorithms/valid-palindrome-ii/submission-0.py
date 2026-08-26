class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # either skip l
                left = s[l+1:r+1] == s[l+1:r+1][::-1]
                # skip r
                right = s[l:r] == s[l:r][::-1]
                return left or right

            l, r = l + 1, r - 1

        return True