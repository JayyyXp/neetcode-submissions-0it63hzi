class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = {}
        for c in hand:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        
        handS = sorted(hand)

        print(handS)

        for j, c in enumerate(handS):

            if count[c] == 0:
                continue
            for i in range(groupSize):
                if (c+i) not in count:
                    return False
                elif count[c+i] < 0:
                    print(j, c, count)
                    return False
                else:
                    count[c+i] -= 1
            if all(v== 0 for v in count.values()):
                return True
            
