class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = []

        for c in s:
            if c.isalnum():
                clean.append(c.lower())
        
        clean_string = ''.join(clean)
        return clean_string == clean_string[::-1]