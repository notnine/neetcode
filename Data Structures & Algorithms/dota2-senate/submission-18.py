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
                dires.append(d + len(senate)) # append n to signify that d's next turn is in the "next" iteration
            else:
                radiants.append(r + len(senate))
        

        return 'Dire' if dires else 'Radiant'