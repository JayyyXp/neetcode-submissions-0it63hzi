class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        memo = {}
        def dfs(l,r):
            if r < l or l >= len(piles) or r < 0:
                return 0
            if (l,r) in memo:
                return memo[(l,r)]
            ret = max(
                piles[l] + dfs(l+2,r),
                piles[l] + dfs(l+1,r-1),
                piles[r] + dfs(l+1,r-1),
                piles[r] + dfs(l,r-2)
            )
            memo[(l,r)] = ret
            return ret

        
        return dfs(0, len(piles)-1) > 0