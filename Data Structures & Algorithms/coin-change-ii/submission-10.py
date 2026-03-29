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
        return dfs(0, 0)