class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dfs(idx, amount):
            if (idx, amount) in cache:
                return cache[(idx, amount)]
            if amount == 0:
                return 1
            if idx > len(coins) - 1:
                return 0
            if amount < 0:
                return 0
            ret = dfs(idx, amount - coins[idx]) + dfs(idx + 1, amount)  
            cache[(idx, amount)] = ret
            return ret

        return dfs(0, amount)