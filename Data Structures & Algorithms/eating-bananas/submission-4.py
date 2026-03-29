class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)

        l, r = 1, maxPile
        ans = r
        while l <= r:
            rate = (r + l) //2
            hoursTaken = 0
            for p in piles:
                hoursTaken += math.ceil(float(p) /rate)
            #print(hoursTaken, rate)
            if hoursTaken <= h:
                ans = rate
                r = rate - 1
            else:
                l = rate + 1
        return ans