class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # search space: eating pace k
        # k \subset {1, max(piles)}

        def can_finish(k: int) -> bool:
            taken = 0
            for p in piles:
                taken += math.ceil(p / k) # check if this math is correct
            
            return taken <= h

        l, r = 1, max(piles)
        last_can_finish = r
        
        while l <= r:
            m = (l + r) // 2
            if can_finish(m):
                # search in the slower half
                last_can_finish = m
                r = m - 1
            else:
                # search in the faster half
                l = m + 1
        
        return last_can_finish