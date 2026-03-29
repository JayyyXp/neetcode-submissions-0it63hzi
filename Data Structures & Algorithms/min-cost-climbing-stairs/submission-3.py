class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ans = [0] * len(cost)
        ans[-1] = cost[-1]
        ans[-2] = cost[-2]

        for i in range(len(ans)-3, -1, -1):
            ans[i] = min(ans[i+1], ans[i+2]) + cost[i]
        print(ans)
        return min(ans[0], ans[1])