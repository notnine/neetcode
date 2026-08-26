class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # return True if we can ship all weights within d days with capcity c
        def valid(c: int) -> bool:
            d = 0
            curr_ship = 0

            for w in weights:
                if curr_ship + w <= c: # if after adding w the ship is still below c
                    curr_ship += w
                else: # we need to ship curr_ship
                    d += 1
                    curr_ship = w
            
            if curr_ship > 0:
                d += 1
            print("c: " + str(c))
            print("d: " + str(d))
            print("curr_ship: " + str(curr_ship))
            return d <= days

        l, r = max(weights), sum(weights)

        while l <= r:
            print("l and r: " + str(l) + ' and ' + str(r))
            m = (l + r) // 2
            can_ship = valid(m)
            if can_ship: # search in left space
                r = m - 1
            else:
                l = m + 1

        return l