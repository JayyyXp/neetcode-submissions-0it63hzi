class Solution:
    def parseTernary(self, expression: str) -> str:
        i = 0
        while i < len(expression):
            if expression[i] == 'T':
                if i == len(expression)-1:
                    return "T"
            
                if expression[i+1] == "?":
                    i += 2
                else:
                    return "T"
            elif expression[i] == 'F':
                if i == len(expression)-1:
                    return "F"
                if expression[i+1] == "?":
                    nxt_colon = 0
                    i += 2
                    while not (nxt_colon == 0 and expression[i] == ":"):
                        if expression[i] == "?":
                            nxt_colon += 1
                        elif expression[i] == ":":
                            nxt_colon -= 1
                        i += 1
                    i += 1
                else:
                    return "F"
            else:
                return expression[i]
        
        return expression[i]