class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        memo = {}
        def dfs(l,r):
            if r < l or l >= len(piles) or r < 0:
                return 0
            if (l,r) in memo:
                return memo[(l,r)]
            ret = max(
                piles[l] + dfs(l+2,r), # Alice left, bob left
                piles[l] + dfs(l+1,r-1), # Alice left, bob right
                piles[r] + dfs(l+1,r-1), # Alice right, bob left
                piles[r] + dfs(l,r-2) # Alice right, bob right
            )
            memo[(l,r)] = ret
            return ret

        total = sum(piles)
        alice = dfs(0, len(piles)-1)
        bob = total - alice
        return  alice > bob