class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = list(s)
        oneCount = 0
        for i, c in enumerate(s):
            if c == "1":
                oneCount += 1
                s[i] = "0"

        oneCount -= 1
        s[-1] = "1"
        i = 0
        while oneCount > 0:
            s[i] = "1"
            oneCount -= 1
            i += 1
        return "".join(s)