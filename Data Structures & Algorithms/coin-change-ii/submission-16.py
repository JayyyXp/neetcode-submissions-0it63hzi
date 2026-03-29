class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        cache = {}
        def dfs(idx, curr):
            if curr == amount:
                return 1
            if curr > amount:
                return 0
            if (idx, curr) in cache:
                return cache[(idx, curr)]
            ret = 0
            for i in range(idx, len(coins)):
                ret += dfs(i, curr + coins[i])
            cache[(idx, curr)] = ret
            return ret
        #return dfs(0, 0)
        #dp = [[0]*(amount+1) for c in coins]
        #for i, _ in enumerate(coins):
        #    dp[i][0] = 1
        #print(dp)
        dp = [0]*(amount+1)
        dp[0] = 1
        for i, c in enumerate(coins):
            dpNew = [0]*(amount+1)
            dpNew[0] = 1
            for a in range(1, amount+1):
                #dp[i][a] = dp[i-1][a]
                dpNew[a] = dp[a]
                if a - c >= 0:
                    #dp[i][a] += dp[i][a-c]
                    dpNew[a] += dpNew[a-c]
            dp = dpNew      

        print(dp)
        #return dp[-1][-1]
        return dp[-1]
