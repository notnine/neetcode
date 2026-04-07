class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # approach 0: keep a list of banned senates where banned[i] = true if banned
        banned = [False] * len(senate)
        radiants = [] # list of the indices of unbanned radiants
        dires = [] # list of the indices of unbanned dires

        for i, s in enumerate(senate):
            if s == 'R':
                radiants.append(i)
            else:
                dires.append(i)

        if not radiants and dires:
            return "Dire"
        if not dires and radiants:
            return "Radiant"
        
        radiants.reverse()
        dires.reverse()
        
        i = 0 
        while i < len(senate):
            if not banned[i]:
                # ban i's first opp
                if senate[i] == 'R':
                    dire = dires.pop()
                    banned[dire] = True
                    if len(dires) == 0:
                        return "Radiant"
                else:
                    radiant = radiants.pop()
                    banned[radiant] = True
                    if len(radiants) == 0:
                        return "Dire"
            i += 1
        
        return "Radiant" if len(radiants) > 0 else "Dire"