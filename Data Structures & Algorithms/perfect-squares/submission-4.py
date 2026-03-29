class Solution:
    def numSquares(self, n: int) -> int:
        
        print(n**0.5)
        ans = 0
        curr = n
        memo = {}
        def dfs(curr): 
            if curr == 0:
                return 0
            if curr in memo:
                return memo[curr]
            ret = float('inf')
            for i in range(1,int(curr**0.5)+1):
                ret = min(
                    1+dfs(curr-i**2),
                    ret
                )
            memo[curr] = ret
            return ret
        return dfs(n)