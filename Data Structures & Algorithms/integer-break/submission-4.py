class Solution:
    def integerBreak(self, n: int) -> int:
        
        memo = {}
        def dfs(s, p, d):
            if s == n and d == 2:
                return p
            if s > n:
                return 0
            if (s,p,d) in memo:
                return memo[(s,p,d)]
            ret = 0
            for i in range(1,n-s+1):
                ret = max(dfs(s+i, p*i, min(2,d+1)), ret)
            memo[(s,p,d)] = ret
            return ret

        return dfs(0, 1, 0)
