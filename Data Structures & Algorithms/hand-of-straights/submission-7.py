class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False


        cardFreq = Counter(hand)
        sortedCards = sorted(cardFreq.keys())
        for card in sortedCards:
            if cardFreq[card] > 0: 
                need = cardFreq[card]

                for i in range(card, card + groupSize): 
                    if cardFreq[i] < need:
                        return False
                    
                    cardFreq[i] -= need

            
        return True