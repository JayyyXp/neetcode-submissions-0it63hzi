class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        nbrFive = 0
        nbrTen = 0
        nbrTwenty = 0
        for bill in bills:
            if bill == 5:
                nbrFive += 1
            elif bill == 10:
                nbrTen += 1
                if nbrFive == 0:
                    return False
                else:
                    nbrFive -= 1
            elif bill == 20:
                nbrTwenty += 1
                if nbrFive < 3:
                    if nbrTen == 0 or nbrFive == 0:
                        return False
                    else:
                        nbrTen -= 1
                        nbrFive -= 1
                else:
                    nbrFive -= 3

        return True
