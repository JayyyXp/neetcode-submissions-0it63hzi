class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = (stoneSum) // 2
        memo = {}
        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (stoneSum - total))
            if (i, total) in memo:
                return memo[(i, total)]
            ret = min(
                dfs(i+1, total),
                dfs(i+1, total+stones[i])
            )
            memo[(i, total)] = ret
            return ret

        return dfs(0,0)