class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        def dfs(i, boughtPrice):
            if i >= len(prices):
                return 0
            if (i, boughtPrice) in memo: 
                return memo[(i, boughtPrice)]
            if boughtPrice == -1:
                ret = max(
                    dfs(i+1, -1),
                    dfs(i+1, prices[i])
                )
        
            elif boughtPrice < prices[i]:
                ret = max(
                    (prices[i] - boughtPrice) + dfs(i+1, -1),
                    dfs(i+1, boughtPrice)
                )
            
            else:
                ret = dfs(i+1, boughtPrice)
            memo[(i, boughtPrice)] = ret
            return ret

        return dfs(0, -1)