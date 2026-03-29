class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        memo = {}
        def dfs(l,r, turn):
            if r < l or l == len(piles) or r == -1:
                return 0
            if (l,r, turn) in memo:
                return memo[(l,r, turn)]
            if turn: #Alice
                ret = max(
                    piles[l] + dfs(l+1,r,False),
                    piles[r] + dfs(l,r-1,False)
                )
            else:
                ret = min(
                    piles[l] - dfs(l+1,r,False),
                    piles[r] - dfs(l,r-1,False)
                )
            memo[(l,r, turn)] = ret
            return ret

        
        return dfs(0, len(piles)-1, True) > 0