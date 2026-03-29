class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k * k
        prev2 = k
        prev1 = k * k
        for i in range(2, n):
            new = (prev2 + prev1) * (k - 1)
            prev2 = prev1
            prev1 = new
        return new
        

