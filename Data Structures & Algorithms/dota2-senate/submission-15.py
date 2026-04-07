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
            print("Dires: " + str(dires))
            print("Radiants: " + str(radiants))
            d, r = dires.popleft(), radiants.popleft()
            print("d, r: " + str([d, r]))
            # if d goes first, then d bans r, else vice versa
            if d < r:
                print("appending " + str(d) + " to dires")
                dires.append(d)
            else:
                print("appending " + str(r) + " to radiants")
                radiants.append(r)
            print()
        
        print("Final Dires: " + str(dires))
        print("Final Radiants: " + str(radiants))
        return 'Dires' if dires else 'Radiant'