class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        stairs = 1
        prev = 1
        count = 1
        while stairs <= n:
            new = prev + 1
            stairs += new
            prev = new
            count += 1
        return count - 1