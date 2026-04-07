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
        
        while len(radiants) > 0 and len(dires) > 0:
            print("Radiants: " + str(radiants))
            print("Dires: " + str(dires))
            print("Banned: " + str(banned))
            print()
            if radiants[-1] < dires[-1]: # then radiant can ban
                dire_to_ban = dires.pop()
                banned[dire_to_ban] = True

            else: # dire bans
                radiant_to_ban = radiants.pop()
                banned[radiant_to_ban] = True
            
        return "Radiant" if len(radiants) > 0 else "Dire"