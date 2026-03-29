class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        memo = {}
        def dfs(i, M, turn): # turn True Alice or False Bob 
            if i >= len(piles):
                return 0
            if (i,M,turn) in memo:
                return memo[(i,M,turn)]
            ret = 0 if turn else float("inf")
            total = 0
            for X in range(1, 2*M+1):
                if i + X - 1 == len(piles):
                    break 
                #maxTake = min(i+X+1, len(piles)-1)
                if turn:
                    total += piles[i+X-1]
                    ret = max(
                        total + dfs(i+X, max(M,X), False),
                        ret
                    )
                else:
                    # Bob plays optimally so he wants to min Alices score
                    ret = min(
                        dfs(i+X, max(M,X), True),
                        ret
                    )
            memo[(i,M,turn)] = ret
            return ret

        return dfs(0, 1, True)