from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # the key is that the curr senate needs to ban the next opp that hasn't gone

        dires = deque()
        radiants = deque()

        for i, c in enumerate(senate):
            if c == 'D':
                dires.append(i)
            else:
                radiants.append(i)
        

        while dires and radiants:
            d, r = dires.popleft(), radiants.popleft()
            # if d goes first, then d bans r, else vice versa
            if d < r:
                dires.append(d)
            else:
                radiants.append(r)
        
        return 'Dires' if dires else 'Radiant'