class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        MOD = 10**9 + 7
        memo = {}
        def dfs(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            if n % 2 == 1:
                return 0
            ret = 0
            for i in range(1, n):
                right = n-i-1
                left = i - 1
                ret = (dfs(left) * dfs(right) + ret) % MOD
            memo[n] = ret
            return ret
            
        return dfs(numPeople) % MOD