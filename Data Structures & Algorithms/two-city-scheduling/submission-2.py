class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        n = N // 2

        costs.sort(key=lambda x: x[0] - x[1])
        ans = 0

        for i in range(n):
            ans += costs[i][0]
            ans += costs[i+n][1]

        return ans