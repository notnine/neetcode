class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort()
        freq = Counter(hand)

        for i in hand:
            if i in freq:
                # try to build out our group
                for j in range(i,i+groupSize):
                    if j not in freq:
                        return False
                    else:
                        freq[j] -= 1
                        if freq[j] == 0:
                            del freq[j]
        
        return True