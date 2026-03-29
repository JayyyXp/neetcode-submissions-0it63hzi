class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonesS = sorted(stones)
           
        while len(stonesS) > 1:
            print(stonesS)
            x = stonesS.pop()
            y = stonesS.pop()
            if x == y:
                continue
            else:
                stonesS.append(abs(x-y))
                stonesS = sorted(stonesS)
        if not stonesS:
            return 0
        return stonesS[0]
            



        
        