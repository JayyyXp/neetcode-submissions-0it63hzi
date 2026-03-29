class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        cs = Counter(s)
        ct = Counter(t)
        #print(cs, ct)

        for char, count in ct.items():
            if cs[char] != count:
                return char