class Solution:
    def isHappy(self, n: int) -> bool:
        curr = n
        seen = set()
        while True:
            print(seen)
            s = 0
            for l in str(curr):
                s += int(l)**2
            if s == 1:
                return True
            if s in seen:
                return False
            seen.add(s)
            curr = s