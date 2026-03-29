class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1s = sorted(s1)
        l, r = 0, len(s1) - 1

        while r < len(s2):
             
            #s2[l:r+1]
            print(s1s, sorted(s2[l:r+1]))
            if s1s == sorted(s2[l:r+1]):
                return True
            l += 1
            r += 1
        return False

        