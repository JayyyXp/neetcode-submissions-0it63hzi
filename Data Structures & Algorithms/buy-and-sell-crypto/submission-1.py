class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur = 0
        mx = 0
        l = 0
        for r in range(len(prices)):
            while prices[r] - prices[l] < 0:
                l += 1
            mx = max(prices[r] - prices[l], mx)

        return mx 