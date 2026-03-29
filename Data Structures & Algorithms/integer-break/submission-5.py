class Solution:
    def integerBreak(self, n: int) -> int:
        
        memo = {}
        def dfs(s,d):
            if s == n and d == 2:
                return 1
            if s > n:
                return 0
            if (s,d) in memo:
                return memo[(s,d)]
            ret = 0
            for i in range(1,n-s+1):
                ret = max(i*dfs(s+i, min(2,d+1)), ret)
            memo[(s,d)] = ret
            return ret

        return dfs(0, 0)
