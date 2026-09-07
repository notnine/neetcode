class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        # bin search
        l, r = 0, num // 2

        while l <= r:
            m = (l + r) // 2
            if m * m == num:
                return True
            elif m * m > num:
                r = m - 1
            else:
                l = m + 1
        
        return False