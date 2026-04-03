class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shifts = 0

        while left != right:
            left = left >> 1
            right = right >> 1
            shifts += 1
        
        return left << shifts
