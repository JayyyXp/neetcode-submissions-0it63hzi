class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        memo = {}
        def dfs(i, prev):
            if i == len(costs):
                return 0
            if (i,prev) in memo:
                return memo[(i,prev)]

            ret = float('inf')
            for j in range(3):
                if j != prev: 
                    ret = min(
                        ret, 
                        costs[i][j] + dfs(i+1, j)
                    )
            memo[(i,prev)] = ret
            return ret
        return dfs(0, -1)