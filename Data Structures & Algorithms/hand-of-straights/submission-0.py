class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        numGroups = len(hand)//groupSize
        count = Counter(hand) #count num elements
        
        for card in sorted(count):
            freq = count[card]
            for i in range(card, groupSize + card):
                if count[i] - freq < 0:
                    return False
                count[i] -= freq
        return True
        
            
            