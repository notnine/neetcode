class Solution:
    def minEnd(self, n: int, x: int) -> int:
        curr = x

        for _ in range(n-1):
            curr = curr + 1
            curr = curr | x
        
        return curr