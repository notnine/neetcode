import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # return True if koko can eat piles with speed s under h hours
        def valid(s: int):
            time = 0
            for pile in piles:
                if s >= pile:
                    time += 1
                else:
                    time += math.ceil(pile / s)
            return time <= h

        l, r = 1, max(piles)
        m = (l + r) // 2

        while l <= r:
            if valid(m):
                r = m - 1
            else:
                l = m + 1
            m = (l + r) // 2
        
        return m + 1