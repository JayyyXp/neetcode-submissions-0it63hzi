class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        s = 0
        e = 1
        ans = 0
        while e < len(prices):

            if prices[e] > prices[s]:
                ans = max(ans, prices[e] - prices[s])
            else:
                s = e
            e += 1

        return ans


