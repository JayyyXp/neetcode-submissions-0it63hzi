class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        banR = 0
        banD = 0
        senate = list(senate)
        while True:
            newSenate = []
            countR = 0
            countD = 0
            for s in senate:
                if s == "R":
                    if banR > 0:
                        banR -= 1
                    else:
                        banD += 1
                        countR += 1
                        newSenate.append(s)
                else:
                    if banD > 0:
                        banD -= 1
                    else:
                        banR += 1
                        countD += 1
                        newSenate.append(s)
            senate = newSenate
            if countR == len(senate):
                return "Radiant"
            if countD == len(senate):
                return "Dire"