class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cache = {}
        def helper(day, canBuy):
            if day > len(prices) - 1:
                return 0
            if (day, canBuy) in cache:
                return cache[(day, canBuy)]
            ret = helper(day + 1, canBuy)
            if canBuy:
                ret = max(ret, helper(day + 1, False) - prices[day])
            else:
                ret = max(ret, helper(day + 2, True)  + prices[day])
            cache[(day, canBuy)] = ret
            return ret
        
        return helper(0, True)