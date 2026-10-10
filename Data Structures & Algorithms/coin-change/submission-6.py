class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        def dfs(curr):
            if curr == 0:
                return 0
            if curr < 0:
                return float('inf')
            if curr in memo:
                return memo[curr]
            ret = float('inf')
            for c in coins:
                ret = min(dfs(curr-c) + 1, ret)
            memo[curr] = ret
            return ret
        ans = dfs(amount)
        return ans if ans != float('inf') else -1