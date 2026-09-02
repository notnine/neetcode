class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, n = 0, len(haystack)
        k = len(needle)

        while i <= n - k:
            if haystack[i:i+k] == needle:
                return i
            i += 1
        
        return -1