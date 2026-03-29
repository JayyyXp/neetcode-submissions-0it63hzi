class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1s = sorted(s1)
        s1Count = {}
        for l1 in s1:
            s1Count[l1] = s1Count.get(l1, 0) + 1
        l, r = 0, len(s1) - 1

        while r < len(s2):
             
            #s2[l:r+1]
            #if s1s == sorted(s2[l:r+1]):
            #    return True
            subCount = {}
            for x in s2[l:r+1]:
                subCount[x] = subCount.get(x, 0) + 1
            if s1Count == subCount:
                return True 
            l += 1
            r += 1
        return False

        