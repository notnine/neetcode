class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = left
        curr = left + 1

        while curr <= right:
            res = res & curr
            curr += 1
        
        return res