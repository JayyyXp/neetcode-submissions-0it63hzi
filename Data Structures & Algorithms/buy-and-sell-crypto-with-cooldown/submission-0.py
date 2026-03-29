class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = [0]
        def helper(day, canBuy, profit):
            if day > len(prices) - 1:
                ans[0] = max(ans[0], profit)
                return 
            #ret = 0
            if canBuy:
                helper(day + 1, False, profit - prices[day])
                helper(day + 1, True, profit)
            else:
                helper(day + 2, True, profit + prices[day])
                helper(day + 1, False, profit)
        helper(0, True, 0)
        return ans[0]