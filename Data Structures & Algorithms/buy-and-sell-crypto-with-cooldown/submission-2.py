class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = [0]
        def helper(day, canBuy):
            if day > len(prices) - 1:
                #ans[0] = max(ans[0], profit)
                return 0
            ret = helper(day + 1, canBuy)
            if canBuy:
                ret = max(ret, helper(day + 1, False) - prices[day])
            else:
                ret = max(ret, helper(day + 2, True)  + prices[day])
            return ret
        
        return helper(0, True)