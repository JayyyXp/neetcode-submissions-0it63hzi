class Solution:
    def integerBreak(self, n: int) -> int:
        
        memo = {}
        def dfs(s):
            if s == 1:
                return 1
            if s < 1:
                return 0
            if s in memo:
                return memo[s]
            ret = 0 if s == n else s
            for i in range(1,s):
                ret = max(i*dfs(s-i), ret)
            memo[s] = ret
            return ret

        return dfs(n)
