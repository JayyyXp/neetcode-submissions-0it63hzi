class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        n = N // 2

        memo = {}
        def dfs(i, toA):
            if (i, toA) in memo:
                return memo[(i, toA)]
            if i == N:
                return 0
            if toA == n:
                # rest have to go B
                ret = sum(costs[j][1] for j in range(i, N))
                return ret
            if (n - toA) == N - i:
                # rest have to go A
                ret = sum(costs[j][0] for j in range(i, N))
                return ret

            ret = min(
                dfs(i+1, toA + 1) + costs[i][0], # go A
                dfs(i+1, toA) + costs[i][1] # go B
            )
            memo[(i, toA)] = ret
            return ret

        return dfs(0, 0)